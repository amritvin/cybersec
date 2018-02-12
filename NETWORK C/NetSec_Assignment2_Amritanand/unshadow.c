#include <stdio.h>
#include <string.h>
#include <stdlib.h>

 int split(char * s1,char * symbol,char * s[]);
 int fileop();
 int main(int argc,char *argv[])
 {
   int in,c=0;
   char *k[100];
   char * d= ":";

   if(argc<3)
   {
     printf("\nusage: ./unshadow [<shadowfile> <passwordfile>]\n\teg:- training-shadow.txt,training-passwd.txt\n");
     exit(0);
   }
   //fileop("training-shadow.txt","training-passwd.txt");
   c=fileop(argv[1],argv[2]); // for file opratrions & unshadow
   if (c)
   printf("\n Created unshadow file on passwordfile.txt\n No.of lines :%d\n",c);
   else
   printf("\n! Some unexpected error occured check the file inputs to the program \n");
   return 0;
 }
int fileop(char fname1[],char fname2[])
{
  int in,in1,count=0;
  char *k[100];
  char *k1[100];
  char mem[100];
  char mem1[100];

  char line[100];

  char * d= ":";
  FILE *f1,*f2,*f3;
  int i=10;
  f1 = fopen(fname1,"r");
  f2 = fopen(fname2,"r");
  f3=fopen("passwordfile.txt","w");
  while(fgets(mem,100,f1)&&(fgets(mem1,100,f2)))
  {count++;
  in=split(mem,d,k);
  char temp[1000];
  strcpy(temp,*(k+1));
  in1=split(mem1,d,k1);
  strcpy(line,*k1);
  strcat(line,":");
  strcat(line,temp);
  strcat(line,":");
  for(int z=2;z<in1;z++){
    strcat(line,*(k1+z));
    if (z+1!=in1)
      strcat(line,":");
  }
  printf("%s\n", line);
  fputs(line,f3);
  fputs("\n",f3);

  }
  return count;
}


 int split(char *s1,char * symbol,char * s[])
 {

  char str[1000];
  strcpy(str,s1);
  char *token = strtok(str, symbol);
  int i=-1;
  while (token != NULL)
  {
      s[++i]=token;
      token = strtok(NULL, symbol);
  }

 return i;

 }
