#include <stdio.h>
#include <openssl/md5.h>

int main()
{
  unsigned char temp[100][50];
    unsigned char c[MD5_DIGEST_LENGTH];
    char *filename="file.c";
    int i;
    FILE *inFile = fopen ("fread.c", "rb");
    MD5_CTX mdContext;
    int bytes;
    unsigned char data[1024];

    if (inFile == NULL) {
        printf ("%s can't be opened.\n", filename);
        return 0;
    }

    MD5_Init (&mdContext);
    int j=0;
    while ((bytes = fread (data, 1, 1024, inFile)) != 0){
    MD5_Update (&mdContext, data, bytes);
    MD5_Final (c,&mdContext);
    for(i = 0; i < MD5_DIGEST_LENGTH; i++)
    { printf("%x", c[i]);
      //sprintf(&temp[j][i],"%02x",c[i]);
    }
        //printf ("hash: %x\n", temp[j]);
    j++;
    printf (" %s\n", filename);

    }
    fclose (inFile);
    return 0;
}
