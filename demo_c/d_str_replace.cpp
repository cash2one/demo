#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/*
 * Search and replace a string with another string , in a string
 * */
char *str_replace(char *search , char *replace , char *subject)
{
    char  *p = NULL , *old = NULL , *new_subject = NULL ;
    int c = 0 , search_size;

    search_size = strlen(search);

    //Count how many occurences
    for(p = strstr(subject , search) ; p != NULL ; p = strstr(p + search_size , search))
    {
        c++;
    }

    //Final size
    c = ( strlen(replace) - search_size )*c + strlen(subject);

    //New subject with new size
    new_subject = (char*)malloc( c*(sizeof(char)) );

    //Set it to blank
    strcpy(new_subject , "");

    //The start position
    old = subject;

    for(p = strstr(subject , search) ; p != NULL ; p = strstr(p + search_size , search))
    {
        //move ahead and copy some text from original subject , from a certain position
        strncpy(new_subject + strlen(new_subject) , old , p - old);

        //move ahead and copy the replacement text
        strcpy(new_subject + strlen(new_subject) , replace);

        //The new start position after this search match
        old = p + search_size;
    }

    //Copy the part after the last search match
    strcpy(new_subject + strlen(new_subject) , old);

    return new_subject;
}

int main(){
    char a[100] = "a(())";
    char b[100] = "a()()";
    char c[100] = "(";
    char d[100] = ")";
    char rc[100] = "\\(";
    char rd[100] = "\\)";

    char aa[100];
    char *aaa = str_replace(c,rc,a);
    printf("%s\n",aaa);
    aaa = str_replace(d,rd,aaa);
    printf("%s\n",aaa);
}
