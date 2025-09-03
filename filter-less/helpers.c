#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int avg;
            // calculate the average pixel value
            // round the number to make sure that the average is correctly rounded
            // to the nearest integer
            // division done in floating-point arithmetic
            avg = round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0);
            // set each color value to the average value
            image[i][j].rgbtRed = avg;
            image[i][j].rgbtGreen = avg;
            image[i][j].rgbtBlue = avg;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // int sepiaRed;
    // int sepiaGreen;
    // int sepiaBlue;

    // for each pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // calculate each new color value using the sepia formula
            float sepiaRed = 0.393 * image[i][j].rgbtRed + 0.769 * image[i][j].rgbtGreen +
                             0.189 * image[i][j].rgbtBlue;
            float sepiaGreen = 0.349 * image[i][j].rgbtRed + 0.686 * image[i][j].rgbtGreen +
                               0.168 * image[i][j].rgbtBlue;
            float sepiaBlue = 0.272 * image[i][j].rgbtRed + 0.534 * image[i][j].rgbtGreen +
                              0.131 * image[i][j].rgbtBlue;

            // ensure the result is an integer between 0 and 255, inclusive
            if (sepiaRed > 255)
            {
                image[i][j].rgbtRed = 255;
            }
            else
            {
                // round the number
                image[i][j].rgbtRed = round(sepiaRed);
            }

            // assign values
            // same as the sepiaRed, but written different
            // round the number
            image[i][j].rgbtGreen = sepiaGreen > 255 ? 255 : round(sepiaGreen);
            image[i][j].rgbtBlue = sepiaBlue > 255 ? 255 : round(sepiaBlue);
        }
    }

    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // first loop is used for rows
    for (int i = 0; i < height; i++)
    {
        // second loop is used to swap the pixels
        for (int j = 0; j < width / 2; j++)
        {
            // temporary variable that stores pixels on certain positions
            RGBTRIPLE aux = image[i][j];

            // swap the pixel at j with the pixel at width - j - 1
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = aux;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // create a copy of the image so it doesn't affect the other pixels
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    // loop through the pixels in the image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int redSum = 0;
            int greenSum = 0;
            int blueSum = 0;
            // avg is a counter
            int counter = 0;

            // loop over the neighbouring pixels
            // by creating the 3x3 grid
            for (int x = -1; x <= 1; x++)
            {
                for (int y = -1; y <= 1; y++)
                {
                    // checking for inbound
                    if ((i + x) >= 0 && (i + x) < height && (j + y) >= 0 && (j + y) < width)
                    {
                        // if it's a valid neighbour, sum its colors
                        redSum += copy[i + x][j + y].rgbtRed;
                        greenSum += copy[i + x][j + y].rgbtGreen;
                        blueSum += copy[i + x][j + y].rgbtBlue;
                        // count the valid neighbours
                        counter++;
                    }
                }
            }

            // assign the average values to the current pixel
            // round them to make sure that the averages are correctly rounded
            // to the nearest integer
            image[i][j].rgbtRed = round((float) redSum / counter);
            image[i][j].rgbtGreen = round((float) greenSum / counter);
            image[i][j].rgbtBlue = round((float) blueSum / counter);
        }
    }

    return;
}
