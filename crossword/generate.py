import sys

from crossword import *

# takes a Crossword object (presumably defined in crossword.py)
# and provides methods to generate, display, and solve the puzzle
class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        # self.crossword is an instance of a Crossword class
        self.crossword = crossword
        # dictionary where keys are Variable objects
        # (representing individual slots in the crossword, like "3-letter word, horizontal, starting at (0,0)")
        self.domains = {
            # var (the Variable object itself) = key in the self.domains dictionary
            # .copy() method creates a shallow copy of the self.crossword.words set
            var: self.crossword.words.copy()
            # iteration part of the dictionary comprehension
            # for every var (which is a Variable object) in the self.crossword.variables set,
            # a new entry will be created in the self.domains dictionary
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Converts a given assignment (a mapping from variables to specific words) into a 2D array of letters,
        representing the filled crossword grid.

        It iterates through each variable-word pair in the assignment
        and places the letters of the word into the correct positions in the letters grid
        based on the variable's starting coordinates and direction (across or down).
        """
        # initialize empty grid (2D height x width) with all cells set to None
        letters = []
        for i in range(self.crossword.height):
            row = []
            for j in range(self.crossword.width):
                row.append(None) # unassigned cell marker
            letters.append(row)

        # fill in the grid with letters from assigned words
        # process each variable (word position) and its assigned word
        for variable, word in assignment.items():

            # determine if this is an ACROSS or DOWN word
            direction = variable.direction

            # Place each letter of the word in the correct grid cells
            for k in range(len(word)):
                # calculate grid coordinates based on word direction:
                # - For DOWN words: increment row (i) while keeping column (j) fixed
                # - For ACROSS words: increment column (j) while keeping row (i) fixed
                # k represents the current letter position in the word (0 = first letter)
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)

                # place the k-th letter of the word at calculated position
                letters[i][j] = word[k]

        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        # generates 2D grid of letters from current assignments
        letters = self.letter_grid(assignment)

        # iterates through each cell in the crossword grid
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                # checks if this cell can hold a letter
                if self.crossword.structure[i][j]:
                    # print the letter if assigned, otherwise print space
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            # new line after each row
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file (simplified version without cell drawing).
        """
        from PIL import Image, ImageDraw, ImageFont

        # grid assignments
        cell_size = 100
        font_size = 80
        bg_color = "white"
        text_color = "black"

        # generate letter grid from current assignments
        letters = self.letter_grid(assignment)

        # create blank white canvas
        img = Image.new(
            "RGB",
            (self.crossword.width * cell_size, # total width
            self.crossword.height * cell_size), # total height
            bg_color
        )

        # drawing tools
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", font_size)

        # loops through every potential cell in the crossword grid
        for i in range(self.crossword.height): # row
            for j in range(self.crossword.width): # column
                # 1 check if cell not blocked
                # 2 check if a letter is assigned there
                if self.crossword.structure[i][j] and letters[i][j]:
                    # calculate center position
                    # column = left edge of current cell + move to horizontal center
                    # for ex, if i = 0 and j = 0:
                    # x = 0 * 80 + 80 // 2
                    # x = 40
                    # // returns an integer
                    x = j * cell_size + cell_size // 2
                    y = i * cell_size + cell_size // 2

                    # Draw text centered in cell
                    draw.text(
                        (x, y),
                        letters[i][j],
                        fill=text_color,
                        font=font,
                        anchor="mm"  # Middle-center alignment
                    )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        # node consistency
        # removes words that don't match variable length
        self.enforce_node_consistency()

        # are consistency (AC3 - ALGORITHM)
        # propagate constraints between connected variables
        self.ac3()

        # backtracking search
        # begin search with empty assignment
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        # ensuring all words in each variable's domain satisfy the variable's unary constraint
        # (in this case, matching the required word length)

        # Iterate through each variable in the domain
        for var in self.domains:

            # Create a set to store words that don't match the variable's length
            to_remove = set()

            # Check each word in the variable's domain
            for word in self.domains[var]:
                # If word length doesn't match variable length, mark for removal
                if len(word) != var.length:
                    to_remove.add(word)

            # Remove all invalid words from the domain
            self.domains[var] -= to_remove

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        # ensures that every remaining word in variable x's domain
        # has at least one compatible word in variable y's domain
        # that satisfies their overlap constraint
        # ACROSS/DOWN only matter for calculating letter positions during revise()

        # track if we modify x's domain
        revised = False

        # get overlap between variables x and y
        overlap = self.crossword.overlaps[x, y]
        # if no overlap, no revision needed
        if not overlap:
            return False

        # get the indices where the variables overlap
        # i for x
        # j for y
        i, j = overlap

        # initialize set to track words to remove from x's domain
        to_remove = set()

        # check each word in x's domain
        for x_word in self.domains[x]:
            # initialize compatible_word_exists with false at the beginning
            compatible_word_exists = False

            # look for at least one compatible word in y's domain
            for y_word in self.domains[y]:
                # check if letters match at overlap
                if x_word[i] == y_word[j]:
                    # if letters match, True and stop looking for matching words
                    compatible_word_exists = True
                    break

            # if no matching word found in y's domain, mark x_word for removal
            if not compatible_word_exists:
                to_remove.add(x_word)

        # remove all incompatible words from x's domain
        if to_remove:
            # set substraction
            self.domains[x] -= to_remove
            # domain was modified
            revised = True

        return revised

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        # when revised returns True, it adds new arcs to the queue
        # arc represents
        # a directional constraint between two variables
        # it is a tuple (x, y), where we want to make them consistent
        # encode puzzle's structure as a constraint network
        # ensures the circled letters match

        # x and y = variable objects
        # one should be across and one should be down

        # create an empty queue for storing arcs
        queue = []

        # initialize queue with all arcs if none provided
        if arcs is None:
            # every variable in the puzzle
            for x in self.domains:
                # every neighbor of x
                for y in self.crossword.neighbors(x):
                    # add the arc to the queue
                    queue.append((x, y))
        else:
            # use provided arcs if available
            queue = list(arcs)

        # process each arc in the queue
        while queue:
            # removes and returns the first element of the list
            # also unpacks the tuple into x and y
            x, y = queue.pop(0)

            # attempt to make x consistent with y
            if self.revise(x, y):
                # if x's domain becomes empty, puzzle is unsolvable
                if not self.domains[x]:
                    return False

                # if x was modified, add all neighboring arcs (except y) back to queue
                for z in self.crossword.neighbors(x):
                    # avoid adding the arc that was just processed
                    if z != y:
                        queue.append((z, x))

        # if queue is empty and no domains are empty, the arc is consistent
        return True

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        # Check if all variables are in the assignment

        # loop through all variables in the puzzle
        for var in self.domains:

            # check if there is a missing assignment
            if var not in assignment:
                # then the assignment isn't complete
                return False

        # if all variables are checked
        # and didn't return False, then all are assigned
        return True

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        # checks if a partial or complete crossword assignment is valid
        # no duplicate words
        # all words match their variable's required length
        # all intersecting words have matching letters that overlap

        # check all values are distinct (no duplicate words)
        words = list(assignment.values())
        # compare lengths of the list of words and the set of words
        # set automatically removes duplicates
        if len(words) != len(set(words)):
            return False # found duplicates

        # check each word matches its variable's length

        # var = required word length
        # var.length = how many letters the word slot must hold
        # the last one = gets the length of the assigned word for that variable
        # ex: assignment[var] = "HELLO", this returns 5
        for var in assignment:
            if var.length != len(assignment[var]):
                return False

        # checks for letter conflicts between intersecting words

        # iterates through each currently assigned variable (word slot) in the puzzle
        for var1 in assignment:
            # finds all neighboring variables that intersect with var1
            for var2 in self.crossword.neighbors(var1):
                # checks if var2 has a word assigned
                if var2 in assignment:
                    # retrieves the intersection point
                    # i for var1
                    # j for var2
                    i, j = self.crossword.overlaps[var1, var2]
                    # compares letters in the intersection
                    if assignment[var1][i] != assignment[var2][j]:
                        # letters differ
                        return False

        return True

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        # this function implements the Least Constraining Value (LCV) heuristic
        # this method orders the possible words for a variable (var) so that
        # 1 words that eliminate the fewest options for neighboring variables come first
        # helps maintain flexibility for future assignments during backtracking

        # calculates how many future choices this value
        # would eliminate from neighboring variables
        # if value[i] ("C" in "CAT") doesn't match neighbor_value[j] ("A" in "ART") = neighbor word is incompatible
        def count_eliminated(value):
            count = 0

            # for each unassigned neighbor
            for neighbor in self.crossword.neighbors(var):
                if neighbor not in assignment:
                    i, j = self.crossword.overlaps[var, neighbor]
                    # count how many neighbor values would be eliminated
                    # neighbor_value[j] = letter at position j in the neighbor's possible word
                    for neighbor_value in self.domains[neighbor]:
                        # letters don't match
                        if value[i] != neighbor_value[j]:
                            count += 1
            return count

        # sort values by least constraining heuristic (ascending)
        return sorted(self.domains[var], key=count_eliminated)

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        # This function selects the next crossword slot (variable) to fill by using two important rules:
        # Minimum Remaining Values (MRV): Pick the slot with the fewest possible words left
        # Degree Heuristic: If there's a tie, pick the one with the most connected neighbors

        # find all unfilled slots
        unassigned = []
        for var in self.domains:
            if var not in assignment:
                unassigned.append(var)

        # sort using selection rules
        def sort_key(var):
            # counts how many possible words are left for this slot
            remaining_words = len(self.domains[var])

            # counts how many other slots this one intersects with
            num_neighbors = len(self.crossword.neighbors(var))

            # -num_neighbors = negative makes Python sort higher numbers first
            return(remaining_words, -num_neighbors)

        # return the best candidate according to the rules
        return min(unassigned, key=sort_key)

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        # implements the core recursive backtracking algorithm for solving the crossword puzzle
        # This method systematically tries possible word assignments for crossword slots until it either:
        # Finds a complete valid solution
        # Exhausts all possibilities and returns None (unsolvable)

        # Base case: complete assignment found
        if self.assignment_complete(assignment):
            # returns the completed puzzle solution
            return assignment

        # select next empty slot using MRV and Degree Heuritics
        var = self.select_unassigned_variable(assignment)

        # try values in heuristic order
        for value in self.order_domain_values(var, assignment):

            # creates new assignment dictionary with this word
            # copy preserves the original assignment for backtracking
            new_assignment = assignment.copy()
            new_assignment[var] = value

            # if consistent
            if self.consistent(new_assignment):
                # recursive search
                result = self.backtrack(new_assignment)
                if result is not None:
                    # if recursion finds a complete solution, returns it up the chain
                    return result

        # No solution found down this branch
        return None

def main():

    # check usage
    # validates correct number of arguments (3 or 4)
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    # grid structure file
    structure = sys.argv[1]
    # word list file
    words = sys.argv[2]
    # optional output image
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    # Crossword() = reads the grid structure and word list
    crossword = Crossword(structure, words)
    # CrosswordCreator() = prepares the solving engine w/ the puzzle
    creator = CrosswordCreator(crossword)
    # runs the full CSP solver (node consistency → AC-3 → backtracking)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            # save as image
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
