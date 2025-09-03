import re

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Regular expression pattern for a valid license plate
    pattern = r"^[A-Z]{2,6}\d*$"

    if not re.fullmatch(pattern, s):
        return False

    # Ensure numbers (if present) do not start with zero
    match = re.search(r"\d+", s)
    if match and match.group(0).startswith("0"):
        return False

    return True

main()
