#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>
int a,b,wait=0;
pthread_mutex_t mutex;
pthread_cond_t cv;

void * printa()
{
		//Critical Section
	pthread_mutex_lock(&mutex);
	if (b!=0)	
	{	wait++;
		pthread_cond_wait(&cv,&mutex);
	}
	printf("a: %d\n",a);
	pthread_mutex_unlock(&mutex);

}
int main()
{
	pthread_mutex_init(&mutex, NULL);	
  	pthread_cond_init(&cv, NULL);
	pthread_t t1;
	pthread_create(&t1,NULL,printa,NULL);
		//Critical section
	pthread_mutex_lock(&mutex);
	printf("ENTER THE VALUE: ");
	scanf("%d",&a);
	b=0;
	if (wait!=0)
		pthread_cond_signal(&cv);
	pthread_mutex_unlock(&mutex);	
	pthread_join(t1,NULL);

	
}
