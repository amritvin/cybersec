#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <netdb.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <arpa/inet.h>
int main(int argc, char *argv[])
{


    int sockfd = 0, n = 0;
    char recvBuff[1024],mybuff[1024];
    struct sockaddr_in serv_addr;

    //if(argc != 7)
    {
        printf("\n Usage: %s <ip of server> \n",argv[0]);
      //  return 1;
    }
    memset(recvBuff, '0',sizeof(recvBuff));
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    memset(&serv_addr, '0', sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    if(!(strcmp(argv[1],"-n")==0))
    {
      serv_addr.sin_port = htons(9090);
    }
    else{
      serv_addr.sin_port = htons(atoi(argv[2]));
    }
    inet_pton(AF_INET, argv[3], &serv_addr.sin_addr);
    connect(sockfd, (struct sockaddr *)&serv_addr, sizeof(serv_addr));
    void filesend(int i)
    {
      FILE *f;
      char c;
      if(i!=1)
      f=fopen(argv[4],"rt");
      if (i==1){
        printf("hai");
        //fclose(f);
        f=fopen(argv[6],"rt");
        fseek(f, atoi(argv[2]), atoi(argv[4]));
      }
      while((c=fgetc(f))!=EOF){
        //printf("%c",c);
        mybuff[i++]=c;
      }
      mybuff[i]='\0';
      fclose(f);
      write(sockfd, mybuff,atoi(argv[2]));
    }
    if(!(strcmp(argv[1],"-n")))
    {
      filesend(0);
    }

    if(!(strcmp(argv[1],"-p")))
    {
      fgets(mybuff, 100, stdin);
      write(sockfd, mybuff, strlen(mybuff));
      while ( (n = read(sockfd, recvBuff, sizeof(recvBuff)-1)) > 0)
      {
        recvBuff[n] = 0;
          if(fputs(recvBuff, stdout) == EOF)
          {
            printf("\n Error : Fputs error\n");
          }
      }

      if(n < 0)
      {
        printf("\n Read error \n");
      }
    }
    if(!(strcmp(argv[1],"-o")))
    {
      filesend(1);
        printf("helo");
    }

    return (0);
}
