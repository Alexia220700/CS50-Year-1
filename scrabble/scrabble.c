#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// introduces the points for each letter of the alphabet 
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
int compute_sc(string word);

int main(void)
{

    // prompts users for two words, two strings
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // calculates the scores
    int sc1 = compute_sc(word1);
    int sc2 = compute_sc(word2);

    // compares the scores and shows which of the two players wins or if their scores are equal
    if (sc1 > sc2)
    {
        printf("Player 1 wins!\n");
    }
    else if (sc2 > sc1)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

// every string is an array
// computes the score for each word
int compute_sc(string word)
{

    // score starts from 0
    int sc = 0;

    // strlen calculates the length of the string
    for (int i = 0; i < strlen(word); i++)
    {
        if (word[i] >= 65 && word[i] <= 90)
        {
            // score equal to score plus index in ASCII minus 65
            //'A' in ASCII is 65, but in POINTS it's 0, only if it's uppercase
            sc = sc + POINTS[word[i] - 'A'];
        }
        else if (word[i] >= 97 && word[i] <= 122)
        {
            // for lowercase, it's minus 97
            sc = sc + POINTS[word[i] - 'a'];
        }
    }
    return sc;
}
