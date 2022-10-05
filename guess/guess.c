#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
	int start,stop,count,guess; int result=0;
	printf("\n\nEnter the starting range :");
	scanf("%d",&start);
	printf("\nEnter the stopping range :");
	scanf("%d",&stop);
	printf("\nEnter the chances :");
	scanf("%d",&count);
	srand(time(NULL));
	int num=rand()%(stop-start)+start;
	printf("\n\n\n\nGame Start\n\n\n");
	while (count>0) {
		printf("\nGuess the number : ");
		scanf("%d",&guess);
		if (num==guess) {
			result=1;
			break;
		} else {
			printf("\n\nTry again\nChances Left : %d\n",--count);
		}
	}
	if (result==1) {
		printf("\n\nYou Guessed the number\n\n");
	} else {
		printf("\n\nGame Over\nThe correct number was %d\n\n",num);
	}
}
