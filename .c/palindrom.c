/**
  *

verybody loves palindromes, but Artur doesn't. 
He has a string S that consists of lowercase English letters ('a' - 'z'). Artur wants to find a substring T of S of the maximal length, so that T isn't a palindrome. 

Input
The input contains a single line, containing string S. String S consists of lower case English letters.

Output
In a single line print the length of T

Constraints 
1 ≤ |S| ≤ 100000

SAMPLE INPUT 
aba
SAMPLE OUTPUT 
2
Explanation
"aba" is a palindrome, but "ab" isn't.

Time Limit:	3.0 sec(s) for each input file.
Memory Limit:	256 MB
Source Limit:	1024 KB

  */

#include <stdio.h>

int main()
{
    char str[100000];
    scanf("%s", &str);
    int first=0;
    int last = strlen(str);
    int small;
    int big = last, count = last;
    for (small = 0; small < last; small++){
        if(str[first]!=str[big-1]){
            break;
        }
        else if(str[last-1]!=str[small]){
            break;
        }
        else if(str[small+1]!=str[big-2]){
            count = (big - small-1);
            break;
        }
        
        count--;
        big--;
    }
    printf("%i",count);
    return 0;
}

  