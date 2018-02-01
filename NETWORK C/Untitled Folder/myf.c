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
#include <getopt.h>


int main(int argc, char *argv[]) {

int option=0;
int l=-1,o=0,p=9090,n=0;

int sockfd = 0;
char recvBuff[1024],mybuff[1024];
struct sockaddr_in serv_addr;
int pck=-1,nck=-1,lck=-1,ock=-1;


void precon()
{int i=-9;
  memset(recvBuff, '0',sizeof(recvBuff));
  sockfd = socket(AF_INET, SOCK_STREAM, 0);
  memset(&serv_addr, '0', sizeof(serv_addr));
  serv_addr.sin_family = AF_INET;
  //printf("connecting to %s\n",argv[argc-2]);
  i=inet_pton(AF_INET, argv[argc-2], &serv_addr.sin_addr);

}

void con()
{int i=-8;
  i=connect(sockfd, (struct sockaddr *)&serv_addr, sizeof(serv_addr));
}
void read_file(int os, int nb)
{
  int i=0;
  FILE *f;
  if(nb==0){
    nb=1023;
  }
  char c;
  f=fopen(argv[argc-1],"r");
  fseek(f, os, SEEK_SET);
  fread(mybuff, nb, 1, f);
  /*while((c=fgetc(f))!=EOF){
    mybuff[i++]=c;
  }
  mybuff[i]='\0';*/
  printf("send: %s\n",mybuff);
  fclose(f);
}
void readmsg(){
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
void filesend(){
    int n=0;
    //fgets(mybuff, 100, stdin);
    write(sockfd, mybuff, strlen(mybuff));
    readmsg();
  }
void portcheck()
{
  if(pck==-1){
  serv_addr.sin_port = htons(p);
  printf("connecting to default port:%d\n",p);
  }
  if(pck==1)
  {
    serv_addr.sin_port = htons(p);
    printf("connecting to specified port:%d\n",p);
}
}
void l_func(int l){
  printf("Listening to 0.0.0.0\n ");
}

void help_message()
{
printf("./a.out [options]{<-n>:no.of bytes to send <-o>:offset <-p> :port} [<ip>][filename] \n");
exit(0);
}
void usage(){
  printf("usage: \n--h help\n -p port\n -o offset\n -n no.of bytes\n ");
}
void client()
{
    portcheck();
    con();
    read_file(o,n);
    filesend();
}
void server(){
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
      portcheck();
      serv_addr.sin_port = htons(p);

      bind(listenfd, (struct sockaddr*)&serv_addr, sizeof(serv_addr));

      listen(listenfd, 10);
      char mybuff[1025],c;
      int i=0;
      while(1){
          connfd = accept(listenfd, (struct sockaddr*)NULL, NULL);
          char recvBuff[1024];
          memset(recvBuff, '0',sizeof(recvBuff));
          int n = 0;
          FILE *fpc;
          fpc= fopen(argv[argc-1],"wb");
          read(connfd, recvBuff, sizeof(recvBuff));

              fwrite(recvBuff,strlen(recvBuff),1,fpc);
              printf("%s\n",recvBuff);

          //fwrite(recvBuff,strlen(recvBuff),1,fp);
          fclose(fpc);
          close(connfd);
          sleep(1);
        }
  }
}
precon();
while ((option = getopt(argc, argv,"hl:n:o:p:")) != -1) {
        switch (option) {
             case 'n' : nck=1;
                        n = atoi(optarg);
		                    //n_func(n);
                 break;
             case 'p' :
                      pck=1;
                      p = atoi(optarg);

                 break;
             case 'l' :
                      lck=1;
                      l =atoi(optarg);
			                l_func(l);
                 break;
             case 'o' :
                      ock=1;
                      o = atoi(optarg);
			                //o_func(o);
                 break;
             case 'h' :
                    //o_func(o);
                    help_message();
                    break;
             default:usage();
                 exit(0);
        }
    }
    if (lck!=1)
    {
      client();

    }
    else{
      server();
    }

}
