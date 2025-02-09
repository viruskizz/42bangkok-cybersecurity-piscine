#include <stdio.h>
#include <string.h>

int main(void)
{
    int is_match;
    char input[100];
    char passwd[] = "__stack_check";
    printf("Please enter key: ");
    scanf("%s", input);
    is_match = strcmp(input, (char *)&input);
    if (is_match == 0)
    {
        printf("Good job.\n");
    }
    else
    {
        printf("Nope.\n");
    }
    return 0;
}
