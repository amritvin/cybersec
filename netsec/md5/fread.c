#include<stdio.h>
#include<stdlib.h>
int main(){
unsigned char buffer[10];
FILE *ptr;

ptr = fopen("hello","rb");  // r for read, b for binary
while(fread(buffer,sizeof(buffer),1,ptr)){
for(int i = 0; i<10; i=i+2)
    {
    printf("%02x %02x", buffer[i],buffer[i+1]);
    printf(" ");
 
    }
    printf("\n");
}
fread(buffer,sizeof(buffer),1,ptr);
for(int i = 0; i<5; i=i+2)
    {int x=1;
    if(i==4)
    {x=0;}
    printf("%02x %02x", buffer[i],buffer[i+x]);
    printf(" ");
 
    }

}


