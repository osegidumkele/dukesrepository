#Dumkele Osegi, PSID 1894081
import sys
import datetime


def find(timeformat):
    months_num = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7,
                  "August": 8,   "September": 9, "October": 10, "November": 11, "December": 12}
    year = timeformat.split(",")[-1].strip()
    month = timeformat.split(",")[0]
    day = timeformat.split(",")[0].split()[-1]
    newmonth = months_num[month]
    return str(newmonth)+"/"+day+"/"+year


while True:
    userinput = input()
    if userinput == "-1":
        break
    print(find(userinput))
