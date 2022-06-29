#Dumkele Osegi PSID 1894081
s = input()
lst = [int(x) for x in s.split(" ") if int(x)>=0]
lst.sort()
for x in lst:
    print(x, end=" ")
