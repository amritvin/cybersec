#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <sys/types.h>
#include <time.h>

int main(int argc, char *argv[])
{
    int listenfd = 0, connfd = 0;
    struct sockaddr_in serv_addr;

    char sendBuff[1025];
    time_t ticks;

    listenfd = socket(AF_INET, SOCK_STREAM, 0);
    memset(&serv_addr, '0', sizeof(serv_addr));
    memset(sendBuff, '0', sizeof(sendBuff));

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_addr.s_addr = htonl(INADDR_ANY);
    serv_addr.sin_port = htons(atoi(argv[1]));

    bind(listenfd, (struct sockaddr*)&serv_addr, sizeof(serv_addr));

    listen(listenfd, 10);
    char mybuff[1025],c;
    int i=0;
    while(1)
    {
        connfd = accept(listenfd, (struct sockaddr*)NULL, NULL);

        /*while((c=getchar()) &&(c!='\n'))
          {
            printf("%c",c);
            mybuff[i]=c;
            i++;
          }
          mybuff[i]='\0';*/
        //ticks = time(NULL);
        //snprintf(sendBuff, sizeof(sendBuff), "%.24s\r\n", ctime(&ticks));
        //write(connfd, sendBuff, strlen(sendBuff));
        char recvBuff[1024];
        memset(recvBuff, '0',sizeof(recvBuff));
        int n = 0;
        while ( (n = read(connfd, recvBuff, sizeof(recvBuff)-1)) > 0)
        {
            recvBuff[n] = 0;
            if(fputs(recvBuff, stdout) == EOF)
            {
                printf("\n Error : Fputs error\n");
            }
            while(fgets(mybuff, 100, stdin)>0)
            {
            write(connfd, mybuff, strlen(mybuff));

            }
        }
        while(fgets(mybuff, 100, stdin)>0)
        {
        write(connfd, mybuff, strlen(mybuff));

        }



        //close(connfd);
        //sleep(1);
     }
}
