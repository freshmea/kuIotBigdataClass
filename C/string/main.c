#include <stdio.h>
// #include <string.h>
#include <stdlib.h>
#include <string.h>
#include "myString.h"

int main()
{
    char *str = (char *)malloc(100 * sizeof(char));
    memset(str, 0, 100 * sizeof(char));
    char *str2 = (char *)malloc(100 * sizeof(char));
    memset(str2, 0, 100 * sizeof(char));

    for (int i = 0; i < 100; i++)
        printf("%c\n", str[i]);
    printf("Hello, World!\n");
    // strcat(str, "abc");
    my_strcat(str, "abc");
    printf("%s\n", str);
    // strcat(str, "def");
    my_strcat(str, "def");
    printf("%s\n", str);
    // printf("%s\n", strcat(str, "ghi"));
    printf("%d\n", my_strcmp("abcde", "cccfe"));
    // strcpy(str2, str);
    my_strcpy(str2, str);
    if (my_strcmp(str, str2) == 0)
    {
        printf("두 스트링 변수는 같다.\n");
    }
    else
    {
        printf("두 스트링 변수는 다르다.\n");
    }
    printf("%d\n", my_strlen(str));
    printf("%d\n", my_strlen(str2));
    my_strcat(str, str2);
    printf("%s\n", str);
    printf("%d\n", my_strlen(str));

    return 0;
}