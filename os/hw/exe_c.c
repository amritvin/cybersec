/*#include<stdio.h>
#include<unistd.h>
void main()
{
 char *cmd = "/bin/ls"; 
 int child_pid = fork(); 
 if (child_pid == 0) { 
 exec(cmd); 
 }
else
 { 
 waitpid(child_pid); 
 }
} */
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdio.h>
int main( void )
{
    int status;
    char *args[2];

    args[0] = "/bin/ls";        // first arg is the full path to the executable
    args[1] = NULL;             // list of args must be NULL terminated

    if ( fork() == 0 )
        execv( args[0], args ); // child: call execv with the path and the args
    else
        wait( &status );        // parent: wait for the child (not really necessary)
printf("%d ", status);
    return 0;
}

 
