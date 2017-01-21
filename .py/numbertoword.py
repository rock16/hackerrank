"""
   The numbers  to  written out in words are 
First character of each word will be capital letter for example: is
Given a number, you have to write it in words.
Input Format
The first line contains an integer , i.e., number of test cases. 
Next  lines will contain an integer .
Constraints
Output Format
Print the values corresponding to each test case.
Sample Input
2
10
17
Sample Output
Ten
Seventeen
"""
def place_value(digits, pos):
    name_of_numbers = ['one','two','three','four','five','six','seven','eight',
                       'nine','ten','eleven','twelve','thirten''fourteen','fifteen',
                       'sixteen','seventeen','eighteen','nineteen','twenty','thirty',
                       'forty','fifty','sixty','seventy','eighty','ninety']
    place_value = ['','thousand','million','billion','trillion']
    final = ''
    L=len(digits)
    if int(digits[0]) and L == 3:
        first = name_of_numbers[int(digits[0])-1]+' '+'hundred'
        final = first
    if int(digits[L-2]) or int(digits[L-1]):
        if (int(digits[L-2])*10) < 21 and int(digits[L-2]):
            second = name_of_numbers[int(digits[(L-2):])-1]
            final = final+' '+second
        else:
            if int(digits[L-2]):
                second = name_of_numbers[(19-3)+int(digits[L-2])]
                final = final+' '+second
            if int(digits[L-1]):
                final = final+' '+name_of_numbers[int(digits[L-1])-1]

    return(final.title()+' '+place_value[pos])

def solve(number):
    t = 0
    result = ''
    while number:
        l = len(number)
        if l >= 3:
            result = place_value(number[(l-3):], t)+' '+result
            number = number[:(l-3)]
        else:
            result = place_value(number, t)+' '+result
            number = ''
        t += 1
    print(result)
