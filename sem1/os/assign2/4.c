
#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>
int wait=0;
pthread_mutex_t mutex;
pthread_cond_t cv;
signed long long int buf;
int wa=-1,wb=-1;

void * printa()
{//Critical Section
	signed long long int a,b;
	pthread_mutex_lock(&mutex);
	if (wait==0)
	{
		wait=2;
		pthread_cond_wait(&cv,&mutex);

	}
	printf("a recieved: %lli \n",buf);
	if(wa==0)
	{
		a=buf;
		buf=0;
		pthread_cond_signal(&cv);
		wb=0;}
	if(wb==0)
	{pthread_cond_wait(&cv,&mutex);
		printf("b recieved: %lli \n",buf);
		b=buf;
		buf=0;
	}
	buf=a*b;
	printf("buf:%lli\n",buf );
	printf("a:%lli,b:%lli\n",a,b);
	pthread_cond_signal(&cv);
	pthread_mutex_unlock(&mutex);

}
int main()
{ signed  long long int k[2];
	pthread_mutex_init(&mutex, NULL);
  	pthread_cond_init(&cv, NULL);
	pthread_t t1;
	pthread_create(&t1,NULL,printa,NULL);

		//Critical section
	pthread_mutex_lock(&mutex);
	printf("ENTER THE Ist VALUE: ");
	scanf("%lli",&k[0]);
	buf=k[0];
	wa++;
	wait++;
	if (wait==2)
	{
		pthread_cond_signal(&cv);
	}
	if (wb!=0)
	{
		pthread_cond_wait(&cv,&mutex);
	}
	printf("ENTER THE  II nd VALUE: ");
	scanf("%lli",&k[1]);
	buf=k[1];

	wb++;
	if(wb==1)
	{
		pthread_cond_signal(&cv);
	}
	if (buf==k[1])
		pthread_cond_wait(&cv,&mutex);

	pthread_mutex_unlock(&mutex);
	printf("mul: %lli ", buf);
 	pthread_join(t1,NULL);



}
