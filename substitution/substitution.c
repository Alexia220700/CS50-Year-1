#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[])
{
    // error message if there are less than 2 or more than 2 arguments
    if (argc != 2)
    {
        printf("./substitution KEY\n");
        return 1;
    }

    // if there are two arguments
    if (argc == 2)
    {
        // get the second argument
        string key = argv[1];

        for (int i = 0; i < 26; i++)
        {
            // checks if all of the inputs are letters
            if (!isalpha(key[i]))
            {
                // outputs an error message if one of the inputs is not a letter
                printf("Key is incorrect. It should only contain letters!\n");
                return 1;
            }
        }

        // checks if the characters are different
        // first string that starts from the first letter
        for (int a = 0; a < strlen(key); a++)
        {
            // second string that starts from the second letter
            //*if it started from the first letter too, there would be an error and a[i] == b[i]*
            for (int b = a + 1; b < strlen(key); b++)
            {
                if (key[a] == key[b])
                {
                    // if characters are not different, the program show this error message
                    printf("Key must contain different characters!\n");
                    return 1;
                }
            }
        }

        // checks if the input is the right length
        if (strlen(key) != 26)
        {
            // if it's not the right length, it will show the error message
            printf("Key must contain 26 characters!\n");
            return 1;
        }

        // asks for plaintext
        string plaintext = get_string("plaintext: \n");

        // the program outputs ciphertext: without a newline
        printf("ciphertext: ");

        // checks if char is lowercase/uppercase/not a letter
        for (int c = 0; c < strlen(plaintext); c++)
        {
            // checks if it's a letter
            if (isalpha(plaintext[c]))
            {
                // checks if it's lowercase
                if (islower(plaintext[c]))
                {
                    // outputs a character
                    printf("%c", tolower(key[plaintext[c] - 'a']));
                }
                // checks if it's uppercase
                else if (isupper(plaintext[c]))
                {
                    // outputs a character
                    printf("%c", toupper(key[plaintext[c] - 'A']));
                }
            }
            // if it's not a letter
            else
            {
                // outputs the rest of the characters
                printf("%c", plaintext[c]);
            }
        }
    }
    printf("\n");
    return 0;
}
