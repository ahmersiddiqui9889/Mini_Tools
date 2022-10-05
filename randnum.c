/*
Author - peppergreen00

Author Notes - suppose you have given range 0 100
then 0 is included and 100 is excluded
*/


#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
	int start,stop;
	printf("Enter the range (format - <start> <stop> ): ");
	scanf("%d%d",&start,&stop);
	srand(time(NULL));
	printf("The number is %d",rand()%stop+start);
}
