yourNumber = input("Give me your number: ")
yourNumber = int(yourNumber)
x = 0
y = 1
while y < yourNumber:
    print(y, end = ",")
    temp1 = y
    temp2 = x + y
    x = temp1
    y = temp2