def simple_number_encrypt(numbers):
    """Encrypts single-digit numbers to letters (1=A, 2=B, ..., 9=I)"""
    encrypted = ""
    for num in numbers:
        if num.isdigit():
            digit = int(num)
            if 1 <= digit <= 9:
                letter = chr(digit + 64)  # A=65 in ASCII
                encrypted += letter
            else:
                encrypted += num  # Keep 0 or other digits as-is
        else:
            encrypted += num  # Keep non-digit characters
    return encrypted


