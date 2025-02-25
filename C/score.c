#include <stdio.h>

int main(void) {
	int korean;
	int english;
	int math;

	printf("insert korean english and math scores\n");
	scanf("%d %d %d", &korean, &english, &math);

	int sum = korean + english + math;
	double avg = sum / 3.0;

	printf("sum is %d\tavg is %.2f\n", sum, avg);

	return 0;
}
