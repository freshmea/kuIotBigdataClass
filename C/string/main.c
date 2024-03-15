#include <stdio.h>
#include <string.h>

int main()
{
    char str[100];
    char str2[100];

    printf("Hello, World!\n");
    strcat(str, "abc");
    printf("%s\n", str);
    strcat(str, "def");
    printf("%s\n", str);
    printf("%s\n", strcat(str, "ghi"));
    printf("%d\n", strcmp("abcde", "abcfe"));
    strcpy(str2, str);
    if (strcmp(str, str2) == 0)
    {
        printf("두 스트링 변수는 같다.\n");
    }
    else
    {
        printf("두 스트링 변수는 다르다.\n");
    }

    return 0;
}