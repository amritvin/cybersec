#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include<crypt.h>
char x[100],y[100];
void xyz(char,char);
int split(char *,char * symbol,char * s[]);
const char * cryptmypass(char password[]);
char gvar[100];
int compare(char x[]);
int count=0;
int main()
{
  FILE *f1,*f3;
  char * d= ":";
  char *k[100];
  char data[100];
  char lin[100];
  char lin2[100];
  int in,y=1;
  f1 = fopen("passwordfile.txt","r");
  f3=fopen("allcrackedpasswords.txt","w");
  while(fgets(data,100,f1))
    {y=1;
    in=split(data,d,k);
    //printf("%s\n",*(k+1));
    strcpy(lin,*(k+1));
    strcpy(lin2,*(k));
    //printf("%s\n",lin);
    y=compare(lin);
    if (y==1){
     printf("%s: ",lin2);
     printf("%s \n",gvar);
     fputs(lin2,f3);
     fputs(": ",f3);
     fputs(gvar,f3);
     fputs("\n",f3);

    }
    }
    fclose(f1);
  return 0;
}

int compare(char x[])
{
  FILE *f2;
  int in;
  const char * hash;
  char lin1[10];
  char data1[100];
  char *k[100];
  char * d1= "\t";
f2=fopen("top250.txt","r");
int y=0;
while(fgets(data1,100,f2))
  {y=0;
  in=split(data1,d1,k);
  //printf("%s\n",*(k+1));
  strcpy(lin1,*(k+3));
  //lin[strlen(lin)];
  lin1[strlen(lin1)-1]='\0';
  //printf("%s\n",lin);
  hash=cryptmypass(lin1);
  //printf("t50: %s\n", hash);
  //printf("pass: %s\n", x);
  if(strcmp(hash,x)==0)
    {count++;
     printf("%d\n",count);
     strcpy(gvar,lin1);
     y=1;
     break;
    }

  }

fclose(f2);
return y;
}
const char * cryptmypass(char password[]){
//printf("%s\n", password);
char *toCrackCiph = crypt(password, "$1$GC");
//printf("%s\n", toCrackCiph);
//char *passwordCiph = crypt(password, "aa");
//printf("%s\n", passwordCiph);
return toCrackCiph;
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
