// Modifies the volume of an audio file

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Number of bytes in .wav header
const int HEADER_SIZE = 44;

// argc ARGument Count == int variable that stores the number of command-line arguments
// argv ARGument Vector == array of character pointers listing
int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Open files and determine scaling factor
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    // atof used to convert a string into a floating-point number
    // and represent the converted floating point nr to its corresponding
    // double value
    float factor = atof(argv[3]);

    // TODO: Copy header from input file to output file

    // array of bytes
    // uint8_t is a type that stores an 8-bit integer
    // n = HEADER_SIZE, which is equal to 44
    uint8_t header[HEADER_SIZE];

    // reads bytes from a file
    fread(header, HEADER_SIZE, 1, input);

    // writes bytes to a file
    fwrite(header, HEADER_SIZE, 1, output);

    // TODO: Read samples from input file and write updated data to output file
    // Create a buffer for a single sample
    //stores a buffer of 16-bits
    int16_t buffer;

    // Read single sample from input into buffer while there are samples left to read
    // using fread() function
    while (fread(&buffer, sizeof(int16_t), 1, input))
    {
        // Update volume of sample
        buffer *= factor;

        // Write updated sample to new file using fwrite()
        fwrite(&buffer, sizeof(int16_t), 1, output);
    }

    //  Close files
    fclose(input);
    fclose(output);
}
