#include <stdio.h>
#include <dirent.h>
#include<string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include<stdlib.h>

int main(void)
{
    struct dirent *de;  // Pointer for directory entry
    char filename[10]; 
    // opendir() returns a pointer of DIR type. 
    DIR *dr = opendir(".");
 
    if (dr == NULL)  // opendir returns NULL if couldn't open directory
    {
        printf("Could not open current directory" );
        return 0;
    }
    // Refer http://pubs.opengroup.org/onlinepubs/7990989775/xsh/readdir.html
     FILE *ptr,*pt,*p;
     p=fopen("hello","rb");
     char helloco[300];
     fread(helloco,300,1,p);     
     char buff[4];
    // for readdir()
    while ((de = readdir(dr)) != NULL){
           // printf("%s\n", de->d_name);
 	    strcpy(filename, de->d_name);
 	    
 	    ptr=fopen(filename,"rb");
 	    //fread(buff,4,1,ptr);
 	   // printf("%s\n", filename);
 	   //printf("%s\n",&(filename[strlen(filename)-4]));
 	   if( strcmp(&(filename[strlen(filename)-4]),".bin")==0)
 	   {
 	   pt=fopen(filename,"wb");
 	   fwrite(helloco,300,1,pt);
 	   fclose(pt);
 	   	
 	   }
 	   fclose(ptr);

}    closedir(dr);   
fclose(p);
/*
char *fd = "hello.asm";
struct stat *buf,*mystat;
char mybu[25];
buf = malloc(sizeof(struct stat));

stat(fd, buf);
stat(mybu, &mystat);
int size = buf->st_size;
printf("%s",mybu);

free(buf);*/


 
    return 0;
}
