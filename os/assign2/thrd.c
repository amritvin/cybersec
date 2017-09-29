#include <stdio.h>
#include <pthread.h>
static void print_os();
pthread_mutex_t mutex;

void* print_xs(void* unused) {
int j;
pthread_mutex_lock(&mutex);
for(j = 0; j < 5; j++)
fputc('x', stderr);
pthread_mutex_unlock(&mutex);
return NULL;
}

static void print_os() {
int i;
pthread_mutex_lock(&mutex);
for(i = 0; i < 5; i++)
fputc('o', stderr);
pthread_mutex_unlock(&mutex);
}


int main() {
pthread_t new,new1;
pthread_create(&new, NULL, &print_xs, NULL);
pthread_create(&new, NULL, &print_os, NULL);
pthread_mutex_lock(&mutex);
pthread_join(new, NULL);
pthread_mutex_unlock(&mutex);
pthread_join(new1, NULL);


return 0;
}
