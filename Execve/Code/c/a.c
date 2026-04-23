# include <unistd.h>
 # include <stdlib.h>
 # include <stdio.h>

 void main () {
 char *binary = "/bin/sh";

 char *arg0 = "/bin/sh";
 char *arg1 = "-c";
 char *arg2 = "ls -al /etc";

 char *argv [] = { arg0 , arg1 , arg2 , NULL };
 char *envp [] = { NULL };

 int r = execve(binary , argv , NULL);
 }