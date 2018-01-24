#include<stdio.h>
#include<stdlib.h>
int main(int argc, char *argv[])
{
	int a,b; 
	a=atoi(argv[1]);
	b=atoi(argv[2]);
	a=a+b;
	printf("%d",a);
	return 0;
}

