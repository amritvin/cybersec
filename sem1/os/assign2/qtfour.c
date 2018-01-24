/*#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>

void * printa(void* arr)
{

	int f[2],s,res;
	f=((int *) arr);
	//s=*((int*)(arr+2));
	printf("%d",f[1]);
	


}
int main()
{

	pthread_t t1;
	int ar[2],
	sum;
	printf("ENTER THE 1st VALUE: ");
	scanf("%d",&ar[0]);
	printf("ENTER THE SECOND VALUE: ");
	scanf("%d",&ar[1]);	
	pthread_create(&t1,NULL,printa,(void*)ar);
	pthread_join(t1,NULL);
	//printf("%d",*sum);

	
}*/
#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>
int wait=0;
pthread_mutex_t mutex;
pthread_cond_t cv;
int buf,wa=-1,wb=-1,c;

void * printa()
{
int j;
	
	//Critical Section
	pthread_mutex_lock(&mutex);
	int a,b;
	printf("a recieved: %d \n",buf);
	if(wa==0) 
	{
		a=buf;
		pthread_cond_signal(&cv);
		wb=0;
				
	}
	if(wb==0)
	{
		pthread_cond_wait(&cv,&mutex);
		printf("b recieved: %d \n",buf); 
		b=buf;
		
	}	
	if (c!=0)	
	{	wait++;
		pthread_cond_wait(&cv,&mutex);
	}
	j=a*b;
	printf("mul: %d a:%d,b:%d\n",j,a,b);
	pthread_mutex_unlock(&mutex);

}
int main()
{ int k[2];
	pthread_mutex_init(&mutex, NULL);	
  	pthread_cond_init(&cv, NULL);
	pthread_t t1;
	pthread_create(&t1,NULL,printa,NULL);
		//Critical section
	pthread_mutex_lock(&mutex);
	printf("ENTER THE Ist VALUE: ");
	scanf("%d",&k[0]);
	buf=k[0];
	wa++;
	if (wb!=0)
	{
		pthread_cond_wait(&cv,&mutex);
		
	}
	printf("ENTER THE  II nd VALUE: ");
	scanf("%d",&k[1]);
	buf=k[1];
	wb++;
	if(wb==1)
	{
		pthread_cond_signal(&cv);
	}
	
	c=0;
	if (wait!=0)
		pthread_cond_signal(&cv);
	pthread_mutex_unlock(&mutex);	
	pthread_join(t1,NULL);

	
}
