#include <stdio.h>
 
int main()
{
    FILE *fp;
    fp = fopen("test.txt", "r");
    char c;
    // Moving pointer to end
    fseek(fp, 100												, 0);
     
    // Printing position of pointer
    while((c=fgetc(fp))!=EOF){
        printf("%c",c);
        //mybuff[i++]=c;
      }
     // mybuff[i]='\0';
    return 0;
}
