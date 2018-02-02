/*
 *  Solution to Producer Consumer Problem
 *  Using Ptheads, a mutex and condition variables
 *  From Tanenbaum, Modern Operating Systems, 3rd Ed.
 */

/*
    In this version the buffer is a single number.
    The producer is putting numbers into the shared buffer
    (in this case sequentially)
    And the consumer is taking them out.
    If the buffer contains zero, that indicates that the buffer is empty.
    Any other value is valid.
*/

#include <stdio.h>
#include <pthread.h>

#define MAX 2			/* Numbers to produce */
pthread_mutex_t the_mutex;
pthread_cond_t condc, condp;
int buffer = 0;
void* producer(void *ptr) {
  int i,a,b;

  for (i = 1; i <= MAX; i++) {
    pthread_mutex_lock(&the_mutex);	/* protect buffer */
   /* while (buffer != 0)		       /* If there is something
					  in the buffer then wait */
            printf("thread : %d", buffer);
      if(i==1)
      {
      pthread_cond_wait(&condp, &the_mutex);
      i++;
      }
      a=buffer;
      if(i==2)
      pthread_cond_wait(&condp, &the_mutex);
      b=buffer;
      pthread_cond_signal(&condp);


    pthread_cond_signal(&condc);	/* wake up consumer */
    pthread_mutex_unlock(&the_mutex);	/* release the buffer */
  }
  pthread_exit(0);
}





int main(int argc, char **argv) {
  pthread_t pro;
  printf("MAIN: \n");
  // Initialize the mutex and condition variables
  /* What's the NULL for ??? */
  pthread_mutex_init(&the_mutex, NULL);
  pthread_cond_init(&condc, NULL);		/* Initialize consumer condition variable */
  pthread_cond_init(&condp, NULL);		/* Initialize producer condition variable */

  // Create the threads

  pthread_create(&pro, NULL, producer, NULL);
	int i;
	int x,y;

  for (i = 1; i <= MAX; i++)
  {
    pthread_mutex_lock(&the_mutex);
    if (i==2)
    {
      pthread_cond_wait(&condc, &the_mutex);
      i++;
    }
    printf("ENTER THE VALUE: \n");
    scanf(" %d", &buffer);
    pthread_cond_signal(&condp);
    if (i==3)
    {
      pthread_cond_wait(&condc, &the_mutex);
    }
    /* wake up consumer */
    pthread_mutex_unlock(&the_mutex);	/* release the buffer */
  }
  printf("ANSWR: %d",buffer);
  pthread_exit(0);
  pthread_join(pro, NULL);

  // Cleanup -- would happen automatically at end of program
  pthread_mutex_destroy(&the_mutex);	/* Free up the_mutex */
  pthread_cond_destroy(&condc);		/* Free up consumer condition variable */
  pthread_cond_destroy(&condp);		/* Free up producer condition variable */

}
