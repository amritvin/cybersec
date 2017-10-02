#include<stdio.h>
int main(){
	char buffer[10];
	int x = 100;
	printf("Enter your name: ");
	gets(buffer);
	if(x == 100){
		printf("Thank you, %s \n", buffer);
	}
	else if(x == 120){
		printf("Is it possible ?\n");
	}
}
