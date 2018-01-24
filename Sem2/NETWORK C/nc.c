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
#include <time.h>

void cleinthandler(int acount, char *vec[] ){
int sockfd = 0, n = 0;
char recvBuff[1024];
struct sockaddr_in serv_addr;

if(acount != 2)
{
    printf("\n Usage: %s <ip of server> \n",vec[0]);
    return 1;
}

memset(recvBuff, '0',sizeof(recvBuff));
if((sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0)
{
    printf("\n Error : Could not create socket \n");
    return 1;
}

memset(&serv_addr, '0', sizeof(serv_addr));

serv_addr.sin_family = AF_INET;
serv_addr.sin_port = htons(5000);

if(inet_pton(AF_INET, vec[1], &serv_addr.sin_addr)<=0)
{
    printf("\n inet_pton error occured\n");
    return 1;
}

if( connect(sockfd, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0)
{
   printf("\n Error : Connect Failed \n");
   return 1;
}

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

return 0;
}

void serverhandler(int acount, char *vec[])
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
serv_addr.sin_port = htons(5000);

bind(listenfd, (struct sockaddr*)&serv_addr, sizeof(serv_addr));

listen(listenfd, 10);

while(1)
{
    connfd = accept(listenfd, (struct sockaddr*)NULL, NULL);

    ticks = time(NULL);
    snprintf(sendBuff, sizeof(sendBuff), "%.24s\r\n", ctime(&ticks));
    write(connfd, sendBuff, strlen(sendBuff));

    close(connfd);
    sleep(1);
 }
}
int main(int argc, char *argv[])
{
  if (argv[2]=="p")
  {
    cleinthandler(argc, argv);
  }
  else
  {
    serverhandler(argc, argv);
  }

}
/*#include <stdio.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <string.h>
#define BUF_SIZE 1024

int main(){
int sockfd;
struct socckaddr_in sockaddr;
char data[BUF_SIZE];
//open the socket
sockfd = socket(AF_INET, SOCK_STREAM, 0);
//set socket address and connect
serverAddr.sin_port = htons(7891);
serverAddr.sin_addr.s_addr = inet_addr("127.0.0.1");
if( connect(sockfd, &sockaddr, sizeof(struct sockaddr_in) < 0){
perror("connect");
exit(1);
}
//send data
write(sockfd, data, BUF_SIZE);
//close the socket
close(sockfd);
}

int serve_sock, client_sock, client_addr_size;
struct sockaddr_in serv_addr, client_addr;
char data[BUF_SIZE];
//open the socket
sockfd = socket(AF_INET, SOCK_STREAM, 0);
//optionally bind() the sock
bind(sockfd, serv_addr, sizeof(struct sockaddr_in));
//set listen to up to 5 queued connections
listen(sockfd, 5);
//could put the accept procedure in a loop to handle multiple clients
//accept a client connection
client_sock = accept(sockfd, &client_addr, &cleint_addr_len);
while(read(client_sock, data, BUF_SIZE)){
// Do something with data
}
//close the connection
close(client_sock);
}*/
