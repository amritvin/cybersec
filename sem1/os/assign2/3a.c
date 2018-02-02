#include <stdio.h>
#include <pthread.h>
static void print_os();
pthread_mutex_t mutex;
int wait=0;
pthread_cond_t cond;
void* print_xs(void* unused) {
	int j;
	pthread_mutex_lock(&mutex);
 	for(j = 0; j < 1000; j++)
 	fputc('x', stderr);
	wait++;
	pthread_cond_signal(&cond);
 	pthread_mutex_unlock(&mutex);
 	return NULL;
}
static void print_os() {
 	int i;
 	for(i = 0; i < 1000; i++)
 	fputc('o', stderr);
}
int main() {
	pthread_mutex_init(&mutex, NULL);
        pthread_cond_init(&cond, NULL);

 	pthread_t new;
 	pthread_create(&new, NULL, &print_xs, NULL);
 	pthread_mutex_lock(&mutex);
	if (wait<=0)
 		pthread_cond_wait(&cond,&mutex);
	print_os();
 	pthread_mutex_unlock(&mutex);
 	pthread_join(new, NULL);
 	return 0;
}
