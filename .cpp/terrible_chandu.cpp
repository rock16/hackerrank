/**
Chandu is a bad student. Once his teacher asked him to print the reverse of a given string. He took three hours to solve it. The teacher got agitated at Chandu and asked you the same question. Can you solve it?

Input:
The first line contains an integer T, denoting the number of test cases.
Each test case contains a string S, comprising of only lower case letters.

Output:
For each test case, print the reverse of the string S.

Constraints:

1 <= T <= 10
1 <= |S| <= 30

SAMPLE INPUT 
2
ab
aba
SAMPLE OUTPUT 
ba
aba
Time Limit:	1.0 sec(s) for each input file.
Memory Limit:	256 MB
Source Limit:	1024 KB
*/

#include <iostream>
#include <string.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    while (n > 0){
        string s;
        int len;
        cin >> s;
        len = s.length();
        for(int i=(len-1); i>=0; i--){
            cout << s[i];
        }
        cout << "\n";
        n = n-1;
    }
    return 0;
}