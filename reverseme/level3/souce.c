/**
 * Decoding Instruction
 * 1. Input string start with 42
 * 2. First of 2 digit input will be converted to '*'
 * 3. Input will be group every 3 char to convert digit to char ascii
 * Example: 00|120|121|122| -> dxyz
 */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void goodjob(void);
void nope(void);

int main(void)
{
    char input[31];
    char passwd[9];
    int scanf_ret;

    printf("Please enter key: ");
    scanf_ret = scanf("%23s", input);
    if (scanf_ret != 1)
    {
        nope();
    }
    if (input[0] != '4' || input[1] != '2')
    {
        nope();
    }
    fflush(stdin);
    memset(passwd, 0, 9);
    passwd[0] = '*';
    int idx = 2;
    int i = 1;
    size_t input_len = strlen(input);
    while (idx < input_len)
    {
        char ascii[3];
        ascii[0] = input[idx];
        ascii[1] = input[idx + 1];
        ascii[2] = input[idx + 2];
        char c = atoi(ascii);
        passwd[i] = (char)c;
        idx = idx + 3;
        i = i + 1;
    }
    passwd[i] = '\0';
    int is_match = strcmp(passwd, "********");
    if (is_match == -2)
    {
        nope();
    }
    else if (is_match == -1)
    {
        nope();
    }
    else if (is_match == 0)
    {
        goodjob();
    }
    else if (is_match == 1)
    {
        nope();
    }
    else if (is_match == 2)
    {
        nope();
    }
    else if (is_match == 3)
    {
        nope();
    }
    else if (is_match == 4)
    {
        nope();
    }
    else if (is_match == 5)
    {
        nope();
    }
    else if (is_match == 0x73)
    {
        nope();
    }
    else
    {
        nope();
    }
    return 0;
}

void goodjob(void)
{
    puts("Good job.");
    return;
}

void nope(void)
{
    puts("Nope.");
    exit(1);
}
