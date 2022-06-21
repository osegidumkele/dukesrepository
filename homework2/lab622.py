#Dumkele Osegi, PSID 1894081
a = int(input())
b = int(input())
c = int(input())

d = int(input())
e = int(input())
f = int(input())

res = False
for x in range(-10, 11):
    for y in range(-10, 11):
        if a * x + b * y == c and d * x + e * y == f:
            print(x,y)
            res = True
if not res:
    print('No solution')

