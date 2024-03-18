#include <stdio.h>
void swap(int *a, int *b)
{
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}
void printStrs(char *strs[], int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("%s\n", strs[i]);
    }
}

int main()
{
    unsigned char result = 0x56 & 0x0F;
    printf("0x%02x\n", result);
    unsigned short price;
    price = 50000;
    int x = 100;
    int y = 200;
    int *a = &x;
    int *b = &y;
    // a = &x;
    // b = &y;
    swap(a, b);
    printf("a = %d, b = %d\n", *a, *b);
    int s = 100;
    void *p = &s;
    *(int *)p = 200;
    printf("s = %d\n", s);
    printf("&s = %p\n", &s);
    printf("p = %p\n", p);

    int nums1[] = {1, 2, 3, 4, 5};
    int nums2[5];
    int *p1 = nums1;
    printf("%p\n", nums1);
    printf("%p\n", nums2);
    printf("%d\n", nums2[0]);
    p1 = nums2;
    printf("%p\n", nums2);
    printf("%d\n", nums2[0]);
    printf("%d\n", nums2[1]);
    printf("%d\n", nums2[2]);
    printf("%d\n", nums2[3]);
    printf("%d\n", nums2[4]);
    char *cities[] = {"Hanoi", "HCM", "Hue", "Da Nang", "Paris"};
    printStrs(cities, 5);
    return 0;
}