#include <stdio.h>
#include <string.h>

int main()
{
    char *m[100];
     void split(char * s1,char symbol,char * s[])
    {
    char str[] =* s1;
    //"plg344:$1$GC$bLGQXmAa7pjS7TkkHvHel.:15434::::::";

    // Returns first token
    char *token = strtok(str, symbol);
    char *strg[6];

    // Keep printing tokens while one of the
    // delimiters present in str[].
    int i=-1;
    while (token != NULL)
    {
        strg[++i]=token;
        //printf("%s\n", token);
        token = strtok(NULL, symbol);
    }
    for(int j=0;j<=i;j++)
    {
      printf("MY paaswd\n");
      printf("%s\n", strg[j]);
    }
    s=strg;
}
    split("plg344:$1$GC$bLGQXmAa7pjS7TkkHvHel.:15434::::::",':',m);
    return 0;
}
