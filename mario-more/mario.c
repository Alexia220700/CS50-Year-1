#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;
    do
    {
        height = get_int("Height:"); // prompt user for height
    }
    while (height < 1 || height > 8);

    for (int i = 0; i < height; i++) // pe coloana pt inaltime
    {
        for (int j = 0; j < height + i + 3; j++)
        {
            if (i + j < height - 1 || j == height || j == height + 1)
                printf(" "); // print spaces
            else
                printf("#"); // print hashes
        }
        printf("\n");
    }
}
