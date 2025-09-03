from cs50 import get_string

text = get_string("Input a text to be verified: ")

letters = 0
# the first word is not counted
words = 1
sentences = 0

i = 0
# len is strlen from C, but in Python
for i in range(len(text)):
    # check if the character is a letter
    if text[i].isalpha():
        letters += 1

    # checks for sentences
    elif text[i] == "." or text[i] == "!" or text[i] == "?":
        sentences += 1

    # checks for spaces to count words
    elif text[i].isspace():
        words += 1

# calculate L
# average number of letters per 100 words in the text
L = letters / words * 100

# calculate S
# average number of sentences per 100 words in the text
S = sentences / words * 100

# round the index for the grades
index = round(0.0588 * L - 0.296 * S - 15.8)

# print the grade level
if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print("Grade ", + index)
