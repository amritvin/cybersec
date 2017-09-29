#include<stdio.h>
#include<pthread.h>
void* phello()
{
        printf("HELLO WORLD");
	
}


int main()
{
        pthread_t t1;
	pthread_create(&t1,NULL,phello,NULL);
        pthread_join(t1,NULL);
}
