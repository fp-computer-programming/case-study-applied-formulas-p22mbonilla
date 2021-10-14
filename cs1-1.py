# Author MB 10/12/2021

x1 = int(input("what is the value of x1: "))
x2 = int(input("what is the value of x2: "))
y1 = int(input("what is the value of y1: "))
y2 = int(input("what is the value of y2: "))

total = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5

total = str(total)

print(total)
