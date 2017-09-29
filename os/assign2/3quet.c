#include <stdio.h>
#include <pthread.h>
static void print_os();
pthread_mutex_t mutex;
void* print_xs(void* unused) {
 int j;
 pthread_mutex_lock(&mutex);
 for(j = 0; j < 1000; j++)
 fputc('x', stderr);
 pthread_mutex_unlock(&mutex);
 return NULL;
}
static void print_os() {
 int i;
 for(i = 0; i < 1000; i++)
 fputc('o', stderr);
}
int main() {
 pthread_t new;
 pthread_create(&new, NULL, &print_xs, NULL);
 pthread_mutex_lock(&mutex);
 print_os();
 pthread_mutex_unlock(&mutex);
 pthread_join(new, NULL);
 return 0;
}
