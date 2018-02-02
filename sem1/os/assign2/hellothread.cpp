#include<stdio.h>
#include<pthread.h>

void* say_hello(void* data)
{
	char *str;
	str = (char*)data;
	printf("%s\n",str);
}
int main()
{
	pthread_t t1,t2;

	pthread_create(&t1,NULL,say_hello,"hello from 1");
	pthread_create(&t2,NULL,say_hello,"hello from 2");
	pthread_join(t1,NULL);
}
