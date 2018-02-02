#include <stdio.h>
extern char **environ;

int main()
{
    for (char **env = environ; *env; ++env)
        printf("%s\n", *env);
}
