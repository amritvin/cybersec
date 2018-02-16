#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <time.h>

int main(int argc, char* argv[])
{
    DIR *mydir;
    struct dirent *myfile;
    struct stat mystat;

    mydir = opendir(argv[1]);
    char buf[512];
    while((myfile = readdir(mydir)) != NULL)
    {
        struct tm *time_stamp=localtime(&mystat.st_mtime);
        sprintf(buf, "%s/%s", argv[1], myfile->d_name);
        stat(buf, &mystat);
        //stat(myfile->d_name, &mystat);   
        mode_t val;

        val=(mystat.st_mode & ~S_IFMT);
        (val & S_IRUSR) ? printf("r") : printf("-");
        (val & S_IWUSR) ? printf("w") : printf("-");    
        (val & S_IXUSR) ? printf("x") : printf("-");
        (val & S_IRGRP) ? printf("r") : printf("-");
        (val & S_IWGRP) ? printf("w") : printf("-");
        (val & S_IXGRP) ? printf("x") : printf("-");
        (val & S_IROTH) ? printf("r") : printf("-");
        (val & S_IWOTH) ? printf("w") : printf("-");
        (val & S_IXOTH) ? printf("x") : printf("-");
        printf("\t%d",mystat.st_nlink);
        printf("\t%d",mystat.st_uid);
        printf("\t%d",mystat.st_gid); 
        printf("\t%d",mystat.st_size);
        char buffer[80];
        strftime(buffer,10,"%b",time_stamp);

        printf("\t%4d %s %2d ", time_stamp->tm_year+1900,buffer,time_stamp->tm_mday);
        printf(" %s\n", myfile->d_name);
    }
    closedir(mydir);
}
