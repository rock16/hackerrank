"""
You are given a string . 
The string contains only lowercase English alphabet characters.

Your task is to find the top three most common characters in the string .

Input Format

A single line of input containing the string .

Constraints


Output Format

Print the three most common characters along with their occurrence count each on a separate line.
Sort output in descending order of occurrence count.
If the occurrence count is the same, sort the characters in ascending order.

Sample Input

aabbbccde
Sample Output

b 3
a 2
"""

def hash_i(char):
    return ord(char)- ord('a')

def find_max(iterable):
    for i in range(3):
        max_index = (max(iterable),iterable.index(max(iterable)))
        iterable[max_index[1]] = 0
        yield max_index

def count_common(N):
    arr = [0] * 26
    for char in N:
        pos = hash_i(char)
        arr[pos] += 1
    
    first_max=next(find_max(arr))
    second_max=next(find_max(arr))
    third_max=next(find_max(arr))

    print(chr(first_max[1]+ord('a')),first_max[0])
    print(chr(second_max[1]+ord('a')),second_max[0])
    print(chr(third_max[1]+ord('a')),third_max[0])
input_string = list(input())
count_common(input_string)
