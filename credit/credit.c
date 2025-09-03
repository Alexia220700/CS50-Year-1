#include <cs50.h>
#include <stdio.h>
int get_digit_sum(long number);
bool is_valid_credit_card(long number);

int main(void)
{
    long number = get_long("Number: ");

    if (is_valid_credit_card(number))
    {
        int length = 0;
        long aux = number;

        while (aux != 0) // lenght of card number
        {
            aux = aux / 10;
            length++;
        }

        // checks if the lenght and first two digits *or first digit for VISA* are correct

        if (length == 15 && (number / 10000000000000 == 34 || number / 10000000000000 == 37))
        {
            printf("AMEX\n");
        }
        else if (length == 16 && (number / 100000000000000 >= 51 && number / 100000000000000 <= 55))
        {
            printf("MASTERCARD\n");
        }
        else if ((length == 13 || length == 16) &&
                 (number / 1000000000000 == 4 || number / 1000000000000000 == 4))
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}

int get_digit_sum(long number)
{
    int sum = 0;
    bool alternate = false;

    while (number > 0)
    {

        int digit = number % 10;
        number = number / 10;

        if (alternate)
        {
            digit = digit * 2; // multiplies every other digit by 2, starting with the number's
                               // second-to-last digit
            if (digit > 9)
            {
                digit = digit - 9;
            }
        }

        sum = sum + digit; // makes a sum of the digits
        alternate = !alternate;
    }
    return sum;
}

bool is_valid_credit_card(long number) // checks if the credit card number is valid, sum%10 == 0
{
    int sum = get_digit_sum(number);

    return (sum % 10 == 0);
}
