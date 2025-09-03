#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // prompts user for text
    string text = get_string("Enter a text: ");

    int letters = 0;
    int words = 1;
    int sentences = 0;

    // using a loop to count words, letters and sentences
    for (int i = 0; i < strlen(text); i++)
    {
        // counting the letters
        if (isalpha(text[i]))
        {
            letters++;
        }
        // counting the sentences
        else if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sentences++;
        }
        // counting the words
        else if (isspace(text[i]))
        {
            words++;
        }
    }

    // calculate L and S
    float L = (float) letters / words * 100;
    float S = (float) sentences / words * 100;

    // round the index for the grades
    int index = round(0.0588 * L - 0.296 * S - 15.8);

    // print the grade level
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}
