/* hello.c */
#include <stdio.h> /* standard input/output */

int main()
{
    char name[32];

    printf("What is your name\n");
    scanf("%s", &name);
    printf("Hello %s\n", name);

    return 0;
}
