/**
 * Decoding Instruction
 * 1. Input string start with 00
 * 2. First of 2 digit input will be converted to 'd'
 * 3. Input will be group every 3 char to convert digit to char ascii
 * Example: 00|120|121|122| -> dxyz
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void ok(void);
void no(void);

int main(void)
{
    char input[24];
    char passwd[9];

    printf("Please enter key: ");
    int scanf_ret = scanf("%23s", input);
    if (scanf_ret != 1)
    {
        no();
    }
    if (input[0] != '0' || input[1] != '0')
    {
        no();
    }
    fflush(stdin);
    memset(passwd, 0, 9);
    passwd[0] = 'd';
    int idx = 2;
    int i = 1;
    while (idx < strlen(input))
    {
        char ascii[3];
        ascii[0] = input[idx];
        ascii[1] = input[idx + 1];
        ascii[2] = input[idx + 2];
        char c = atoi(ascii); // convert alphabet index y to int char
        passwd[i] = (char)c;  // convert int char to char
        idx += 3;
        i++;
    }
    passwd[i] = '\0';
    if (strcmp(passwd, "delabere") == 0)
        ok();
    else
        no();
    return 0;
}

void ok(void)
{
    puts("Good job.");
}

void no(void)
{
    puts("Nope.");
    exit(1);
}
