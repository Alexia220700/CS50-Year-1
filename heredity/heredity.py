import csv
import itertools
import sys

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}


def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]


def joint_probability(people, one_gene, two_genes, have_trait):
    def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return the joint probability of the given gene distribution and trait expression.

    Args:
        people: Dictionary where keys are names and values are dictionaries with 'mother' and 'father' keys
        one_gene: Set of people with one copy of the gene
        two_genes: Set of people with two copies of the gene
        have_trait: Set of people who exhibit the trait

    Returns:
        float: Joint probability of all specified conditions
    """
    joint_prob = 1.0  # Initialize joint probability to 1 (multiplicative identity)

    for person in people:
        # Determine how many copies of the gene this person has
        if person in one_gene:
            gene_count = 1
        elif person in two_genes:
            gene_count = 2
        else:
            gene_count = 0

        # Calculate probability for gene count
        parents = people[person]

        if not parents['mother'] and not parents['father']:
            # Person has no parents - use base probability from PROBS["gene"]
            gene_prob = PROBS["gene"][gene_count]
        else:
            # Person has parents - calculate inheritance probability
            mother = parents['mother']
            father = parents['father']

            # Determine mother's probability of passing the gene
            if mother in two_genes:
                mother_passes = 1 - PROBS["mutation"]  # Will pass gene (may mutate)
            elif mother in one_gene:
                mother_passes = 0.5  # 50% chance to pass gene
            else:  # mother has 0 genes
                mother_passes = PROBS["mutation"]  # Only passes if mutation occurs

            # Determine father's probability of passing the gene
            if father in two_genes:
                father_passes = 1 - PROBS["mutation"]
            elif father in one_gene:
                father_passes = 0.5
            else:  # father has 0 genes
                father_passes = PROBS["mutation"]

            # Calculate probability for each gene count scenario
            if gene_count == 0:
                gene_prob = (1 - mother_passes) * (1 - father_passes)
            elif gene_count == 1:
                gene_prob = (mother_passes * (1 - father_passes) +
                           (1 - mother_passes) * father_passes)
            else:  # gene_count == 2
                gene_prob = mother_passes * father_passes

        # Calculate probability for trait expression
        trait_expressed = person in have_trait
        trait_prob = PROBS["trait"][gene_count][trait_expressed]

        # Multiply both probabilities into the joint probability
        joint_prob *= gene_prob * trait_prob

    return joint_prob

def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    for person in probabilities:
        if person in one_gene:
            probabilities[person]["gene"][1] += p
        elif person in two_gene:
            probabilities[person]["gene"][2] += p
        else:
            probabilities[person]["gene"][0] += p

        # Update trait probability distribution
        if person in have_trait:
            probabilities[person]["trait"][True] += p
        else:
            probabilities[person]["trait"][False] += p

def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    for person in probabilities:
        # Normalize gene distribution
        gene_dist = probabilities[person]["gene"]
        gene_total = sum(gene_dist.values())
        if gene_total > 0:  # Avoid division by zero
            for count in gene_dist:
                gene_dist[count] /= gene_total

        # Normalize trait distribution
        trait_dist = probabilities[person]["trait"]
        trait_total = sum(trait_dist.values())
        if trait_total > 0:  # Avoid division by zero
            for has_trait in trait_dist:
                trait_dist[has_trait] /= trait_total



if __name__ == "__main__":
    main()
