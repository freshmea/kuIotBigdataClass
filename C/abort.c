#include <stdio.h>
#include <stdlib.h>

int main(void){
    abort();
    exit(-1);
    printf("This line will not be executed");
    return 0;
}