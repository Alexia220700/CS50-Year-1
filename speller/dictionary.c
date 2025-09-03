#include <ctype.h> //for character handling functions
#include <math.h>  //for mathematical functions
#include <stdbool.h>  //for boolean
#include <stdint.h>  //for fixed-width integers type
#include <stdio.h>  //for input/output functions
#include <stdlib.h>  //for memory allocation
#include <string.h>  //for string manipulation
#include <strings.h>  //for string comparison

#include "dictionary.h"

//define the number of buckets in the hash table
#define N 20000

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// declares hash table
node *table[N];

//initialize word_count for dictionary
unsigned int word_count = 0;

// Hash function prototype
unsigned int hash(const char *word);

// Function to load the dictionary
bool load(const char *dictionary)
{
    // Open dictionary file
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        return false;
    }

    //buffer for a word
    //the additional character is for the null terminator "\0"
    char word[LENGTH + 1];

    //reads words from the dictionary file
    //until EOF, end of file
    while (fscanf(file, "%s", word) != EOF)
    {
        //creates a new node for each word
        //and allocates memory for it
        node *new_node = malloc(sizeof(node));

        //if the new node is empty
        if (new_node == NULL)
        {
            return false;
        }

        //copy the word into the new node
        strcpy(new_node->word, word);

        //hash the word to obtain a hash value
        unsigned int index = hash(word);

        //insert node into the hash table
        //sets next pointer to point to the current head of the linked list
        new_node->next = table[index];
        //updates the head of the linked list to point to the new node
        table[index] = new_node;

        //increment word count
        word_count++;
    }

    //close dictionary file
    fclose(file);
    return true;
}

// Function to check if a word is in the dictionary
bool check(const char *word)
{
    //hash the word to obtain a hash value
    unsigned int index = hash(word);

    //access linked list at that index in the hash table
    node *cursor = table[index];

    //go through the linked list, looking for the word
    while (cursor != NULL)
    {
        //compare word in dictionary to input word
        //case-insensitive comparison
        if (strcasecmp(word, cursor->word) == 0)
        {
            //word found
            return true;
        }
        //updates cursor to point to the next node in the linked list
        cursor = cursor->next;
    }

    //word not found
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    //hash the first letter of the word
    //convert the first letter of the word to lowercase
    return tolower(word[0]) - 'a';
}

// Function to return the number of words in the dictionary
unsigned int size(void)
{
    return word_count;
}

// Function to unload the dictionary from memory
bool unload(void)
{
    //iterate over the hash table
    for (int i = 0; i < N; i++)
    {
        // Free linked lists
        node *cursor = table[i];
        while (cursor != NULL)
        {
            //store current node
            node *temp = cursor;
            //move to the next node
            cursor = cursor->next;
            //free the memory of the current node
            free(temp);
        }
    }
    return true;
}
