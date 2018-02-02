#include <stdio.h>
#include <string.h>

 void split(char * s1,char * symbol,char * s[]);

 int main(){
   char *k[100];
   char * d= ":";
   split("plg344:$1$GC$bLGQXmAa7pjS7TkkHvHel.:15434::::::",d,k);
   printf("%s\n",*k);

   return 0;
 }

 void split(char *s1,char * symbol,char * s[]){

  char str[1000];
  strcpy(str,s1);
  char *token = strtok(str, symbol);
  int i=-1;
  while (token != NULL)
  {
      //printf("%s\n", token);
      s[++i]=token;
      token = strtok(NULL, symbol);
  }

 }
