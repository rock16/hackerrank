"""
Objective 
Today, we're working with binary numbers. Check out the Tutorial tab for learning materials and an instructional video!

Task 
Given a base- integer, , convert it to binary (base-). Then find and print the base- integer denoting the maximum number of consecutive 's in 's binary representation.

Input Format

A single integer, .

Constraints

Output Format

Print a single base- integer denoting the maximum number of consecutive 's in the binary representation of .

Sample Input 1

5
Sample Output 1

1
Sample Input 2

13
Sample Output 2

2
"""
#!/bin/python3

import sys


n = int(input().strip())
(count, maxim)=(0,0)

while n > 0:
    rem = n%2
    if rem == 1:
        count += 1
    elif rem == 0:
        count = 0
    if maxim < count:
        maxim = count
    n = n//2        
print(maxim)
