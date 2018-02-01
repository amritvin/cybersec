#include <stdio.h>

int  main(int argc, char const *argv[]) {
int i=0;
FILE *fp,*f;
char c,mybuff[1024];
f=fopen(argv[argc-1],"r");
fseek(f, 2, SEEK_SET);
fread(mybuff, 100, 1, f);
fclose(f);/*
while((c=fgetc(f))!=EOF){
  mybuff[i++]=c;
}
mybuff[i]='\0';*/
fp=fopen("args2.txt","w");
fwrite(mybuff,sizeof(mybuff)-1,1,fp);
printf("%s",mybuff);
fclose(fp);
}
