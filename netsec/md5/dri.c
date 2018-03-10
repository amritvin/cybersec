#include <stdio.h>
#include <dirent.h>
#include<string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include<stdlib.h>
#include <openssl/md5.h>
void md(char *filename);
unsigned char temp[100];
unsigned char c[MD5_DIGEST_LENGTH];
struct storage{
	char fn[50];
	unsigned char mhash[50];
}store[100];


int main(void)
{
    struct dirent *de;  // Pointer for directory entry
    char filename[10];
    char store[100][100]; 
    // opendir() returns a pointer of DIR type. 
    DIR *dr = opendir(".");
 
    if (dr == NULL)  // opendir returns NULL if couldn't open directory
    {
        printf("Could not open current directory" );
        return 0;
    }
    // Refer http://pubs.opengroup.org/onlinepubs/7990989775/xsh/readdir.html
     FILE *ptr,*pt;
     char helloco[300];   
     char buff[4];
     unsigned char * mdh;
     int i;
    // for readdir()
    int m=0;
    while ((de = readdir(dr)) != NULL){
           // printf("%s\n", de->d_name);
 	    strcpy(filename, de->d_name);
 	    //fread(buff,4,1,ptr);
 	    printf("%s      \t", filename);
 	    strcpy(store[m].fn,filename);
 	   //printf("%s\n",&(filename[strlen(filename)-4]));
            md(filename);
            for(i = 0; i < MD5_DIGEST_LENGTH; i++) 
    		{
    			printf("%02x", c[i]);
    		}
    	    strcpy(store[m].mhash,filename);
    	    m++;
 	    printf("\n");	
 	   }


    closedir(dr);
  return 0;
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

}




void md(char *filename){
    //char *filename="file.c";
    int i;
    FILE *inFile = fopen (filename, "rb");
    MD5_CTX mdContext;
    int bytes;
    unsigned char data[1024];

    if (inFile == NULL) {
        printf ("%s can't be opened.\n", filename);
        //return 0;
    }

    MD5_Init (&mdContext);
    while ((bytes = fread (data, 1, 1024, inFile)) != 0)
        MD5_Update (&mdContext, data, bytes);
    MD5_Final (c,&mdContext);
    /**for(i = 0; i < MD5_DIGEST_LENGTH; i++) 
    {
    printf("%x", c[i]);
    sprintf(temp,"%x",c[i]);
   
    }*/
    //printf ("filename: %s\n", filename);
    //printf (" md5: from function %s\n", temp);
    fclose (inFile);

    }
