#include <stdio.h>

int main(void)
{
	int width, height;
	
	printf("insert number\n");
	scanf("%d %d", &width, &height);
	
	double extent = width * height / 2;
	
	printf("extent is %f\n", extent);
	
	return 0;
}
