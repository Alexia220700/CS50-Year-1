#include <stdio.h>
#include <stdlib.h>
// for uint8_t
#include <stdint.h>

// one command line argument
int main(int argc, char *argv[])
{
    // accept a single comment-line argument
    //ex: ./recover Hello
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    // opens the memory card in read mode only
    FILE *f = fopen(argv[1], "r");

    // checks if memory card opens correctly
    // if it doesn't, it shows a message
    if (f == NULL)
    {
        // printf("Could not open file %s.\n", argv[1]);
        return 2;
    }

    // create a buffer to store all the filenames
    uint8_t buffer[512];
    // size of file = 8 bytes
    char filename[8];

    // counts every JPEG file
    int counter = 0;

    //initialize string img with NULL
    FILE *img = NULL;

    // while there's still data left to read from the memory card
    // fread(data, size, number, inptr)
    // fread checks in 512 byte blocks
    while (fread(buffer, 1, 512, f) == 512)
    {
        // checks if there are any JPEG headers in the array / buffer
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff &&
            ((buffer[3] & 0xf0) == 0xe0))
        // the buffer[3] part clears out the last 4 bits by equaling them to 0 and only checks the
        // first 4 bits
        {
            // closes previous file if it exists
            if (img != NULL)
            {
                fclose(img);
            }

            // creates a new file with a sequential name
            sprintf(filename, "%03i.jpg", counter);
            // opens file in write mode
            img = fopen(filename, "w");

            if (img == NULL) // check if the JPEG file was created successfully
            {
                fclose(f); // close the memory card file before exiting
                return 1;
            }

            // writes the new buffer in the new file
            //in 512 byte block
            fwrite(buffer, 1, 512, img);

            // counts each JPEG header
            counter++;
        }
        // if there is no new header
        else if (img != NULL)
        {
            // contuines to write in this buffer
            fwrite(buffer, 1, 512, img);
        }
    }

    // closes previous file if it exists
    if (img != NULL)
    {
        fclose(img);
    }

    // close the memory card
    fclose(f);
    return 0;
}
