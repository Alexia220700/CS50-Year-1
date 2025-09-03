def calculate_girank(family_tree, damping=0.85, max_iter=100, tol=1e-6):
    # family_tree = dictionary representing the family relationship

    # damping = parameter, represents the probability that an individual's
    # influence is passed on to their children

    # max_iter = the maximum number of iterations the algorithm will run

    # tol = tolerance level for convergence
    # if the total change in ranks between two consecutive iterations is less than this value,
    # the algorithm stops, assuming it has converged
    from collections import defaultdict # used to create parents dictionary, where the children are the keys

    # Collect all unique individuals (parents and children)
    people = set(family_tree.keys())
    for children in family_tree.values():
        people.update(children)
    # stores them in a list called people
    people = list(people)
    # This ensures that everyone in the tree gets a rank

    # Initialize equal rank for each individual
    # If there are N people, each person starts with a rank of 1/N
    N = len(people)
    ranks = {person: 1.0 / N for person in people}

    # Create reverse mapping: child -> list of parents
    # To calculate a child's rank, you need to know who their parents are
    # This section creates a parents dictionary where each key is a child, and its value is a list of their direct parents
    parents = defaultdict(list)
    for parent, children in family_tree.items():
        for child in children:
            parents[child].append(parent)

    # Count the number of children each parent has and store it in the dictionary num_children
    # a parent's influence is divided among their children
    # Initialize an empty dictionary to store the results
    num_children = {}

    # Loop through each parent and their children in the family tree
    for parent, children in family_tree.items():
        # Count how many children this parent has
        children_count = len(children)

        # Store the count in the dictionary with parent as the key
        num_children[parent] = children_count

    # Iteratively update the GIRank values
    # running for a maximum number of iterations or until convergence
    for iteration in range(max_iter):
        # Start with a base rank for each person
        # represents the "random jump" probability, ensuring that even individuals
        # with no parents or children still have some base influence
        new_ranks = {person: (1 - damping) / N for person in people}

        # Add influence from each person's parents
        for person in people:
            for parent in parents.get(person, []):
                # the new_ranks for a person are updated by adding a portion of their parent's current ranks
                # divided by the number of children and multiplied with the damping factor
                new_ranks[person] += damping * (ranks[parent] / num_children[parent])

        # Calculate the total change in rank values
        # abs = absolute value, returns the non-negative value of a number
        delta = sum(abs(new_ranks[p] - ranks[p]) for p in people)
        ranks = new_ranks

        # Stop if the changes are small enough (converged)
        # converged = the ranks have stabilized
        if delta < tol:
            break

    # Return the final ranks, sorted by descending influence
    return dict(sorted(ranks.items(), key=lambda x: -x[1]))
    # explained and rewritten: return dict(sorted(ranks.items(), key=lambda item: item[1], reverse=True))

# for seeing how the code works in terminal window
# Sample family tree
family_tree = {
    "Alice": ["Bob", "Carol"],
    "Bob": ["Dave", "Eve"],
    "Carol": ["Frank"],
    "Eve": ["Grace"],
    "Frank": ["Heidi"]
}

# Run GIRank
ranks = calculate_girank(family_tree)

# Output results
print("Genetic Influence Ranking (GIRank):")
for person, score in ranks.items():
    print(f"{person}: {score:.4f}")
    # or with rounding: print(person + ": " + str(round(score, 4)))
