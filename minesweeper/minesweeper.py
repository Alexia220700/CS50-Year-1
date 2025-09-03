import itertools # creates iterators for efficient looping (count, cycle, repeat)
import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    # initialize the board as a class
    def __init__(self, height=8, width=8, mines=8):
        # INITIALIZE ATTRIBUTES FOR THE GAME BOARD
        # Set initial width of the Minesweeper board
        self.width = width
        # Set initial height of the Minesweeper board
        self.height = height
        # empty set to store the (row, column) tuples of where the mines are located
        self.mines = set()

        # CREATE THE GAME BOARD
        # A 2D list (list of lists) representing the game board
        self.board = []
        # Iterate over the height of the board to create rows
        for i in range(self.height):
            # Initialize an empty row.
            row = []
            # Iterate over the width of the board to create cells in each row
            for j in range(self.width):
                # Initially, no cell contains a mine (False)
                row.append(False)
            # Add the created row to the game board.
            self.board.append(row)

        # RANDOMLY PLACE THE MINES ON THE BOARD (8 MINES)
        while len(self.mines) != mines:
            # Generate a random row index within the board's height.
            i = random.randrange(height)
            # Generate a random column index within the board's width.
            j = random.randrange(width)
            # Check if the current cell does not already contain a mine
            if not self.board[i][j]:
                # Add the coordinates of the mine to the set of mines
                self.mines.add((i, j))
                # Mark the cell on the board as containing a mine (True)
                self.board[i][j] = True

        # Initialize an empty set to keep track of the mines the player has found (flagged).
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        # Iterate over each row of the board.
        for i in range(self.height):
            print("|", end="")
            # Iterate over each cell in the current row
            for j in range(self.width):
                # Check if the current cell contains a mine
                if self.board[i][j]:
                    # Print 'X' to indicate a mine.
                    print("X|", end="")
                else:
                    # Print '_' to indicate an empty cell
                    print("_|", end="")
                print(" ")

    def is_mine(self, cell):
        """
        Checks if a given cell contains a mine.
        """
        # Unpack the row and column indices from the cell tuple
        i, j = cell
        # Return True if the board at the given indices is True (contains a mine), False otherwise.
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Initialize a counter for the number of nearby mines.
        count = 0

        # Loop over all cells within one row above and below the given cell
        for i in range(cell[0] - 1, cell[0] + 2):
            # Loop over all cells within one column to the left and right of the given cell
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself.
                if (i, j) == cell:
                    continue

                # Check if the neighboring cell is within the bounds of the board
                if 0 <= i < self.height and 0 <= j < self.width:
                    # Check if the neighboring cell contains a mine
                    if self.board[i][j]:
                        # Increment the count of nearby mines
                        count += 1

        # Return the total count of nearby mines.
        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        # Return True if the set of found mines is equal to the set of all mines, False otherwise.
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        # Initialize the set of cells in the sentence
        self.cells = set(cells)
        # Initialize the amount of mines known to be among those cells
        self.count = count

    def __eq__(self, other):
        # Defines equality for Sentence objects based on their cells and count
        # equal if their cells sets are the same and their count values are the same
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        # Define a string representation for Sentence objects
        # ex: {(0,0), (0,1)} = 1
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        # If the number of cells in the sentence equals the mine count and the count is greater than zero,
        # then all cells in the sentence must be mines
        if len(self.cells) == self.count and self.count > 0:
            return set(self.cells)
        # Otherwise, no cells are definitively known to be mines based on this sentence alone
        return set()

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        # If the mine count in the sentence is zero, then all cells in the sentence must be safe
        if self.count == 0:
            return set(self.cells)
        # Otherwise, no cells are definitively known to be safe based on this sentence alone.
        return set()

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        # Check if the given cell is one of the cells included in this sentence
        if cell in self.cells:
            # If it is, remove the cell from the set of cells in the sentence
            self.cells.remove(cell)
            # Decrement the count of potential mines in the sentence
            self.count -= 1

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        # Check if the given cell is one of the cells included in this sentence
        if cell in self.cells:
            # If it is, update the sentence so that the cell is no longer considered
            self.cells.remove(cell)
        # If the cell is not in the sentence, no action is needed for this sentence


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):
        # Set initial height of the Minesweeper board for the AI
        self.height = height
        # Set initial width of the Minesweeper board for the AI
        self.width = width

        # Keep track of which cells have been clicked on by the AI
        self.moves_made = set()

        # Keep track of cells known by the AI to be safe.
        self.safes = set()
        # Keep track of cells known by the AI to be mines.
        self.mines = set()

        # List of sentences (logical statements) about the game known to be true by the AI.
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine in the AI's knowledge, and updates all knowledge
        to reflect that this cell is a mine.
        """
        # Add the cell to the set of known mines.
        self.mines.add(cell)
        # Iterate through all the sentences in the AI's knowledge.
        for sentence in self.knowledge:
            # For each sentence, update it to reflect that the given cell is a mine.
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe in the AI's knowledge, and updates all knowledge
        to reflect that this cell is safe.
        """
        # Add the cell to the set of known safe cells.
        self.safes.add(cell)
        # Iterate through all the sentences in the AI's knowledge.
        for sentence in self.knowledge:
            # For each sentence, update it to reflect that the given cell is safe.
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper game reveals a new cell.
        Updates the AI's knowledge based on the revealed cell and the number of
        adjacent mines.
        """
        # 1 Mark the cell as a move that has been made
        self.moves_made.add(cell)

        # 2 Mark the cell as safe, as it was revealed and did not contain a mine
        self.mark_safe(cell)

        # 3 Get all neighboring cells of the revealed cell.
        neighbors = set()
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):
                # Exclude the cell itself from its neighbors.
                if (i, j) == cell:
                    continue
                # Ensure the neighbor is within the bounds of the board.
                if 0 <= i < self.height and 0 <= j < self.width:
                    neighbors.add((i, j))

        # 4 Only consider neighbors that are currently unknown (not already safe or known mines)
        new_cells = set()
        adjusted_count = count
        for neighbor in neighbors:
            # If a neighbor is a known mine, decrement the count of nearby mines for the sentence
            if n in self.mines:
                adjusted_count -= 1
            # If a neighbor is not a known safe cell, add it to the set of new cells for the sentence
            elif neighbor not in self.safes:
                new_cells.add(neighbor)

        # 5 Add a new sentence to the AI's knowledge representing the relationship
        #   between the unknown neighboring cells and the adjusted count of mines
        if new_cells:
            self.knowledge.append(Sentence(new_cells, adjusted_count))

        # 6 Repeat the process of inferring new safe and mine cells based on the current knowledge,
        #    and updating the knowledge accordingly, until no new inferences can be made
        changed = True
        while changed:
            changed = False

            # a Collect sets of newly identified safe and mine cells from all known sentences
            new_safes = set()
            new_mines = set()
            for sentence in self.knowledge:
                new_safes |= sentence.known_safes()
                new_mines |= sentence.known_mines()

            # b Mark these newly identified safe and mine cells in the AI's internal state
            for cell in new_safes:
                if cell not in self.safes:
                    self.mark_safe(cell)
                    changed = True

            for cell in new_mines:
                if cell not in self.mines:
                    self.mark_mine(cell)
                    changed = True

            # c Perform inference based on subset relationships between sentences
            #    If one sentence's cells are a subset of another's, we can create a new sentence
            #    representing the difference
            new_sentences = []
            for s1 in self.knowledge:
                for s2 in self.knowledge:
                    # Avoid comparing a sentence to itself or empty sentences
                    if s1 == s2 or not s1.cells or not s2.cells:
                        continue
                    # If the cells in s1 are a subset of the cells in s2.
                    if s1.cells.issubset(s2.cells):
                        # Calculates the difference in cells
                        diff_cells = s2.cells - s1.cells
                        # Calculates the difference in the mine count
                        diff_count = s2.count - s1.count
                        # Creates a new sentence representing this difference
                        new_sentence = Sentence(diff_cells, diff_count)
                        # If this new sentence is not already known, add it
                        if new_sentence not in self.knowledge and new_sentence not in new_sentences:
                            new_sentences.append(new_sentence)
                            changed = True

            # Add all the newly inferred sentences to the AI's knowledge.
            self.knowledge.extend(new_sentences)

        # 7 Remove any sentences from the knowledge that have no cells left
        # Create a new list to store the sentences that are still relevant
        updated_knowledge = []

        # Iterate over each sentence in the current knowledge base
        for s in self.knowledge:
            # Check if the sentence still contains any unknown cells
            if s.cells:  # An empty set (or any empty collection) evaluates to False in a boolean context
                # If it still has cells, it's a relevant sentence, so add it to the updated list
                updated_knowledge.append(s)

        # Replace the old knowledge list with the new, cleaned-up list
        self.knowledge = updated_knowledge

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        # Iterate over all cells on the board.
        for i in range(0, self.width):
            for j in range(0, self.height):
                # If a cell is known to be safe and has not been clicked yet, return it as a safe move
                if (i, j) in self.safes and (i, j) not in self.moves_made:
                    return (i, j)
        # If no safe moves are currently known, return None
        return None

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
        """
        # Initialize an empty list to store valid moves
        valid_moves = []
        # Iterate over all cells on the board
        for i in range(self.width):
            for j in range(self.height):
                # Check if the current cell has not been moved to
                # and is not a known mine
                cell = (i, j)
                if cell not in self.moves_made and cell not in self.mines:
                    # add the cell to the list of valid moves
                    valid_moves.append(cell)

        # Return a random move from the list of valid moves if there are any, otherwise return None
        if valid_moves:
            return random.choice(valid_moves)
        else:
            return None
