#include "helpers.h"
#include <math.h>
#include <stdint.h> //used for rounding

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
    // RGBTRIPLE means uint_8 rgbtRed; uint_8 rgbtBlue; uint_8 rgbtGreen;
    RGBTRIPLE copy[height][width];

    // Copy the original image into the copy array
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    //loop for height
    for (int i = 0; i < height; i++)
    {
        //loop for width
        for (int j = 0; j < width; j++)
        {
            //initialize sums with 0
            int redSum = 0;
            int greenSum = 0;
            int blueSum = 0;

            // used for counting neighbouring pixels
            int counter = 0;

            // loop over the neighbouring pixels
            // by creating the 3x3 grid
            for (int x = -1; x <= 1; x++)
            {
                for (int y = -1; y <= 1; y++)
                {
                    // checking for valid neighbouring pixels
                    // trying to make sure that it's not a pixel outside the boundaries
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
            // round them to make sure that the averages are correct
            image[i][j].rgbtRed = round((float) redSum / counter);
            image[i][j].rgbtGreen = round((float) greenSum / counter);
            image[i][j].rgbtBlue = round((float) blueSum / counter);
        }
    }

    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    // create a copy of the image so it doesn't affect the other pixels
    // RGBTRIPLE means uint_8 rgbtRed; uint_8 rgbtBlue; uint_8 rgbtGreen;
    RGBTRIPLE copy[height][width];

    //loop for height
    for (int i = 0; i < height; i++)
    {
        //loop for width
        for (int j = 0; j < width; j++)
        {
            //make a copy
            copy[i][j] = image[i][j];
        }
    }

    // loop through the pixels in the image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // initializing each gradient sum with 0
            int gxRed = 0;
            int gxGreen = 0;
            int gxBlue = 0;
            int gyRed = 0;
            int gyBlue = 0;
            int gyGreen = 0;

            // making two arrays
            //using the Sobel operator
            int gx[9] = {-1, 0, 1, -2, 0, 2, -1, 0, 1};
            int gy[9] = {1, 2, 1, 0, 0, 0, -1, -2, -1};

            // counter is used for checking if there are any neighbouring pixels
            // reset counter for each pixel
            int counter = 0;

            // looping over the neighbouring pixels
            // by creating the 3x3 grid
            for (int x = -1; x <= 1; x++)
            {
                for (int y = -1; y <= 1; y++)
                {
                    // checking for valid neighbouring pixels, in bounds
                    if ((i + x) >= 0 && (i + x) < height && (j + y) >= 0 && (j + y) < width)
                    {
                        // making copies, used in the final gradient magnitude
                        gxRed += copy[i + x][j + y].rgbtRed * gx[counter];
                        gxGreen += copy[i + x][j + y].rgbtGreen * gx[counter];
                        gxBlue += copy[i + x][j + y].rgbtBlue * gx[counter];

                        gyRed += copy[i + x][j + y].rgbtRed * gy[counter];
                        gyGreen += copy[i + x][j + y].rgbtGreen * gy[counter];
                        gyBlue += copy[i + x][j + y].rgbtBlue * gy[counter];
                    }
                    // counter for valid member
                    counter++;
                }
            }
            // calculate the final gradient magnitude for each channel
            int redValue = round(sqrt(gxRed * gxRed + gyRed * gyRed));
            int greenValue = round(sqrt(gxGreen * gxGreen + gyGreen * gyGreen));
            int blueValue = round(sqrt(gxBlue * gxBlue + gyBlue * gyBlue));

            // claim the values from 0 to 255
            // if value is more than 255, then value turns into 255
            if (redValue > 255)
            {
                //the max value is 255
                //used to ensure there won't be any error 
                redValue = 255;
            }
            if (greenValue > 255)
            {
                greenValue = 255;
            }
            if (blueValue > 255)
            {
                blueValue = 255;
            }

            // assign new values to image
            image[i][j].rgbtRed = redValue;
            image[i][j].rgbtGreen = greenValue;
            image[i][j].rgbtBlue = blueValue;
        }
    }
    // return after all pixels are processed
    return;
}
