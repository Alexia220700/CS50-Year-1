import emoji

# prompt user for a string in english
str = input("Input: ")

# convert emoji codes/aliases to emojis
# emoji is the library
# the language='alias' ensures that both codes (:thumbs_up:) and aliases (:thumbsup:) are supported
emojized_text = emoji.emojize(str, language='alias')

# output the emojized text
print("Output:", emojized_text)


