import csv
import sys


def main():
    # Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python3 dna.py database.csv sequence.txt")
        sys.exit(1)  # exit if there are not exactly two arguments

    # Read the database file into a variable
    rows = []
    with open(sys.argv[1], newline='') as file:
        # creates a list of dictionaries from the file
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)

    # Read DNA sequence file into a variable
    with open(sys.argv[2], 'r') as f:
        dna_sequence = f.read()

    # Extract STR sequences from the first row of the CSV (exclude 'name' column)
    str_sequences = reader.fieldnames[1:]

    # Find longest match of each STR in the DNA sequence
    str_counts = {}
    for str_sequence in str_sequences:
        str_counts[str_sequence] = longest_match(dna_sequence, str_sequence)

    # Check database for matching profiles
    match_found = False
    for row in rows:
        # Check if STR counts match the individual in the database
        match = True
        for str_sequence in str_sequences:
            if int(row[str_sequence]) != str_counts[str_sequence]:
                match = False
                break

        if match:
            print(row['name'])
            match_found = True
            break  # exit the loop after finding the first match

    # If no match was found
    if not match_found:
        print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for the most consecutive runs of subsequence
    for i in range(sequence_length):
        count = 0
        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        while True:
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    return longest_run


if __name__ == "__main__":
    main()
