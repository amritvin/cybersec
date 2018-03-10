#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include<crypt.h>
#include<stdlib.h>
char x[100],y[100];
int split(char *,char * symbol,char * s[]);
const char * cryptmypass(char password[]);
char gvar[100];
int compare(char x[]);
int count=0;
char fhash[100];
char fdict[100];
int main(int argc, char *argv[])
{
  FILE *f1,*f3;
  char * d= ":";
  char *k[100];
  char data[100];
  char lin[100];
  char lin2[100];
  int in,y=1;
  int option=0;
  if (argc <3 )
  {
    printf("usage:\nGuessword -i [<unshadow file>]  -d [<dictionary >]\n\teg : guessword -d t50dictionary.txt  -i passwordfile.txt \n");
    exit(0);
  }
  while ((option = getopt(argc, argv,"d:i:")) != -1) {
          switch (option) {
               case 'd' : strcpy(fdict,optarg);
                   break;
               case 'i' : strcpy(fhash,optarg);
                   break;
               default: printf("usage:\nGuessword -i [<unshadow file>]  -d [<dictionary >]\n\teg : guessword -d t50dictionary.txt  -i passwordfile.txt\n");
               exit(0);
          }
      }
  f1 = fopen(fhash,"r");
  f3=fopen("allcrackedpasswords.txt","w");
  while(fgets(data,100,f1))
    {y=1;
    in=split(data,d,k);
    strcpy(lin,*(k+1));
    strcpy(lin2,*(k));
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
    if(count)
    printf("\n Write successfully cracked-password into allcrackedpasswords.txt\n No.of lines :%d\n",count);
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
f2=fopen(fdict,"r");
int y=0;
while(fgets(data1,100,f2))
  {y=0;
  in=split(data1,d1, );
  strcpy(lin1,*(k+3));
  lin1[strlen(lin1)-1]='\0';
  hash=cryptmypass(lin1);
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
char *toCrackCiph = crypt(password, "$1$GC");
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
     s[++i]=token;
     token = strtok(NULL, symbol);
 }
return i;
}
