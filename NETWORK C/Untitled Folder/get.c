#include<stdio.h>
#include <getopt.h>
#include<stdlib.h>
int main(int argc, char *argv[]) {
int option=0,a=-1,b=-1,l=-1,p=-1;
while ((option = getopt(argc, argv,"apl:b:")) != -1) {
        switch (option) {
             case 'a' : a = 0;
			printf("a%d\n",a);
			printf("%d",option);
                 break;
             case 'p' : p = 0;
			printf("p%d\n",p);
			printf("%d",option);
                 break;
             case 'l' : l = atoi(optarg);
			printf("l%d\n",l); 
			printf("%d",option);
                 break;
             case 'b' : b = atoi(optarg);
			printf("b%d\n",b);
			printf("%d",option);
                 break;
             default: printf("INVALID"); 
                 exit(0);
        }
    }
printf("%d haai",option);
}
