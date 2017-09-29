#include <stdio.h>
#include <stdlib.h>

int main ()
{
 
   printf("USER : %s\n",getenv("USER"));
   printf("HOME : %s\n", getenv("HOME"));
   printf("PWD : %s\n",getenv("PWD"));
   printf("PATH : %s\n", getenv("PATH"));



   return(0);
}
