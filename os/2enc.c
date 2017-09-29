#include<stdio.h>
#include<string.h>
int main(int argc, char **argv, char** envp)
{
  char** env;
  char str[10000];
  for (env = envp; *env != 0; env++)
  {
    char* thisEnv = *env;
    strcpy(str,thisEnv);
    if strcmp(str,'USER')
	
	{
		printf("%s"str);
	}
	if strcmp(str,'HOME')

        {
                printf("%s"str);
        }
	if strcmp(str,'PWD')

        {
                printf("%s"str);
        }
	if strcmp(str,'PATH')

        {
                printf("%s"str);
        }


        
  }
  return(0);
}
