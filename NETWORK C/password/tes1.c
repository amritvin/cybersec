#include <stdio.h>
#include <string.h>

 int split(char * s1,char * symbol,char * s[]);
 void fileop();
 int main()
 {
   int in;
   char *k[100];
   char * d= ":";
   //in=split("plg344:$1$GC$bLGQXmAa7pjS7TkkHvHel.:15434::::::",d,k);
   fileop("training-shadow.txt","training-passwd.txt");
   return 0;
 }
void fileop(char fname1[],char fname2[])
{
  int in,in1;
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
  f3=fopen("passwrd.txt","w");
  while(fgets(mem,100,f1)&&(fgets(mem1,100,f2)))
  {
  in=split(mem,d,k);
  //printf("%s\n",*(k+1));
  char temp[1000];
  strcpy(temp,*(k+1));
  //printf("%s\n",temp);
  in1=split(mem1,d,k1);
  //printf("%s\n",*(k1));
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
}


 int split(char *s1,char * symbol,char * s[])
 {
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
 return i;
 }
