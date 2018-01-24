#include<stdio.h>
int main()
{
  char mybuff[1025],c;
  int i=0;
  while((c=getchar()) &&(c!='\n'))
    {
      printf("%c",c);
      mybuff[i]=c;
      i++;
    }
    mybuff[i]='\0';
    printf("%s",mybuff);
}
