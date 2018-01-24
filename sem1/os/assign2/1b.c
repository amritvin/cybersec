#include <stdio.h>
#include <stdlib.h>

int main ()
{
   setenv("ROOT","root",1);
   printf("ROOT: %s\n", getenv("ROOT"));



   return(0);
}
