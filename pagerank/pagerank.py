import os
import random
import re
import sys

# Constants for the PageRank algorithm
DAMPING = 0.85  # The probability that the surfer follows a link (vs. random jump)
SAMPLES = 10000  # Number of samples for the sampling method


def main():
    """
    Main function that orchestrates the PageRank computation using both methods.
    """
    # Check for correct command-line usage (expects directory name)
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")

    # Parse the directory and build the web page corpus (which pages link to which)
    corpus = crawl(sys.argv[1])

    # Compute PageRank using the sampling method
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")  # Print sorted results with 4 decimal places

    # Compute PageRank using the iterative method
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and extract links between them.
    Returns a dictionary representing the web corpus:
    - Keys: page filenames
    - Values: set of pages that the key page links to
    """
    pages = dict()

    # Process each HTML file in the directory
    for filename in os.listdir(directory):
        # Skip non-HTML files
        if not filename.endswith(".html"):
            continue

        # Read the file contents and find all <a href> links
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            # Regex to find all href attributes in anchor tags
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            # Store links (excluding self-links)
            pages[filename] = set(links) - {filename}

    # Filter to only include links that point to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages  # Only keep links that exist in our corpus
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Calculate the probability distribution for the next page visit.
    Returns a dictionary:
    - Keys: all pages in corpus
    - Values: probability of visiting that page next
    """
    probability_distribution = {}
    num_pages = len(corpus)

    # Handle pages with no outgoing links (treat as linking to all pages)
    if not corpus[page]:
        # Equal probability for all pages
        for p in corpus:
            probability_distribution[p] = 1.0 / num_pages
        return probability_distribution

    # Probability from random jump (1-damping_factor distributed evenly)
    random_prob = (1 - damping_factor) / num_pages

    # Probability from following links (damping_factor distributed among links)
    link_prob = damping_factor / len(corpus[page])

    # Calculate total probability for each page
    for p in corpus:
        # Start with random jump probability
        probability_distribution[p] = random_prob
        # Add link probability if this page is linked from current page
        if p in corpus[page]:
            probability_distribution[p] += link_prob

    return probability_distribution


def sample_pagerank(corpus, damping_factor, n):
    """
    Estimate PageRank by simulating random surfer behavior over n samples.
    Returns a dictionary with each page's estimated importance.
    """
    # Initialize count for each page
    page_counts = {page: 0 for page in corpus}

    # Start at random page and count it
    current_page = random.choice(list(corpus.keys()))
    page_counts[current_page] += 1

    # Perform n-1 more samples (first sample already counted)
    for _ in range(1, n):
        # Get probabilities for next page from transition model
        probabilities = transition_model(corpus, current_page, damping_factor)

        # Randomly choose next page based on probabilities
        current_page = random.choices(
            list(probabilities.keys()),  # Possible pages
            weights=list(probabilities.values()),  # Their probabilities
            k=1  # We want one selection
        )[0]  # random.choices returns a list, take first element

        # Increment count for the selected page
        page_counts[current_page] += 1

    # Convert counts to probabilities by dividing by total samples
    return {page: count / n for page, count in page_counts.items()}


def iterate_pagerank(corpus, damping_factor):
    """
    Compute PageRank iteratively until ranks stabilize.
    Returns a dictionary with each page's calculated importance.
    """
    num_pages = len(corpus)
    threshold = 0.001  # Consider converged when changes are < 0.001
    # Initialize all ranks to equal probability
    ranks = {page: 1 / num_pages for page in corpus}

    while True:
        new_ranks = {}
        max_diff = 0  # Track maximum change between iterations

        for page in corpus:
            # Start with random jump component
            new_rank = (1 - damping_factor) / num_pages

            # Sum contributions from pages linking to this page
            for linking_page, links in corpus.items():
                # If linking page has no links, treat as linking to all pages
                num_links = len(links) if links else num_pages
                if page in links or not links:  # Handle pages with no links
                    new_rank += damping_factor * ranks[linking_page] / num_links

            new_ranks[page] = new_rank
            # Update maximum difference seen this iteration
            max_diff = max(max_diff, abs(new_rank - ranks[page]))

        ranks = new_ranks  # Update all ranks at once

        # Stop iterating if changes are small enough
        if max_diff < threshold:
            break

    # Normalize ranks to sum to 1 (account for floating point imprecision)
    total = sum(ranks.values())
    return {page: rank / total for page, rank in ranks.items()}


if __name__ == "__main__":
    main()
