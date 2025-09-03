#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max voters and candidates
#define MAX_VOTERS 100
#define MAX_CANDIDATES 9

// preferences[i][j] is jth preference for voter i
int preferences[MAX_VOTERS][MAX_CANDIDATES];

// Candidates have name, vote count, eliminated status
typedef struct
{
    string name;
    int votes;
    bool eliminated;
} candidate;

// Array of candidates
candidate candidates[MAX_CANDIDATES];

// Numbers of voters and candidates
int voter_count;
int candidate_count;

// Function prototypes
bool vote(int voter, int rank, string name);
void tabulate(void);
bool print_winner(void);
int find_min(void);
bool is_tie(int min);
void eliminate(int min);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: runoff [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX_CANDIDATES)
    {
        printf("Maximum number of candidates is %i\n", MAX_CANDIDATES);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
        candidates[i].eliminated = false;
    }

    voter_count = get_int("Number of voters: "); // ask for nr of voters
    if (voter_count > MAX_VOTERS)                // if an uncertain number is entered
    {
        printf("Maximum number of voters is %i\n", MAX_VOTERS);
        return 3;
    }

    // Keep querying for votes                           //asks for votes *rank from voters
    // voter_count
    for (int i = 0; i < voter_count; i++)
    {

        // Query for each rank
        for (int j = 0; j < candidate_count; j++) // by rank 1 2 3... candidate_count
        {
            string name = get_string("Rank %i: ", j + 1);

            // Record vote, unless it's invalid
            if (!vote(i, j, name))
            {
                printf("Invalid vote.\n");
                return 4;
            }
        }

        printf("\n");
    }

    // Keep holding runoffs until winner exists           //try to find winner
    while (true)
    {
        // Calculate votes given remaining candidates
        tabulate();

        // Check if election has been won
        bool won = print_winner();
        if (won)
        {
            break;
        }

        // Eliminate last-place candidates          //last place candidate is eliminated
        int min = find_min();
        bool tie = is_tie(min);

        // If tie, everyone wins                   //if equal, everyone wins?
        if (tie)
        {
            for (int i = 0; i < candidate_count; i++)
            {
                if (!candidates[i].eliminated)
                {
                    printf("%s\n", candidates[i].name);
                }
            }
            break;
        }

        // Eliminate anyone with minimum number of votes
        eliminate(min);

        // Reset vote counts back to zero
        for (int i = 0; i < candidate_count; i++)
        {
            candidates[i].votes = 0;
        }
    }
    return 0;
}

// Record preference if vote is valid
bool vote(int voter, int rank, string name)
{
    // check if candidate's name exists in the array
    for (int i = 0; i <= candidate_count - 1; i++)
    {
        // checking if the candidate is valid
        if (strcmp(candidates[i].name, name) == 0)
        {
            // if the candidate's name is valid, record preference
            preferences[voter][rank] = i;
            return true;
        }
    }
    return false;
}

// Tabulate votes for non-eliminated candidates
void tabulate(void)
{
    // TODO
    // first loop goes through every voter
    for (int i = 0; i <= voter_count - 1; i++)
    {
        // second loop goes through the candidates
        for (int j = 0; j < candidate_count; j++)
        {
            int candidate_index = preferences[i][j];

            // verify if the candidate is eliminated or not
            if (!candidates[candidate_index].eliminated)
            {
                // if candidate is not eliminated, the vote is added to him
                candidates[candidate_index].votes++;
                break;
            }
        }
    }
    return;
}

// Print the winner of the election, if there is one
bool print_winner(void)
{
    // TODO
    for (int i = 0; i <= candidate_count - 1; i++)
    {
        if (candidates[i].votes > voter_count / 2)
        {
            printf("%s\n", candidates[i].name);
            return true;
        }
    }

    return false;
}

// Return the minimum number of votes any remaining candidate has
int find_min(void)
{
    // TODO
    int min = voter_count;

    for (int i = 0; i <= candidate_count - 1; i++)
    {

        if (!candidates[i].eliminated)
        {
            if (candidates[i].votes < min)
            {
                min = candidates[i].votes;
            }
        }
    }

    return min;
}

// Return true if the election is tied between all candidates, false otherwise
bool is_tie(int min)
{
    // int sum used for checking if all of the candidates have equal votes
    int sum = 0;
    int sum2 = 0;

    // loop through candidates array
    for (int i = 0; i < candidate_count; i++)
    {
        // counting the non-eliminated candidates
        if (!candidates[i].eliminated)
        {
            // number of candidates
            sum++;

            // compare number of votes to min
            if (candidates[i].votes == min)
            {
                // if they are equal, count them
                sum2++;
            }
        }
    }

    // compare the number of candidates with the number of
    // candidates with minimum votes
    if (sum == sum2)
    {
        return true;
    }
    else
    {
        return false;
    }

    return false;
}

// Eliminate the candidate (or candidates) in last place
void eliminate(int min)
{
    // TODO
    for (int i = 0; i <= candidate_count - 1; i++)
    {
        if (candidates[i].votes == min)
        {
            candidates[i].eliminated = true;
        }
    }

    return;
}
