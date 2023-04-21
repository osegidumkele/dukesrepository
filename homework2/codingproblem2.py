#Dumkele Osegi, Python program to traverse through a .txt file for dates
import sys
import datetime


def find(timeformat):
    months_num = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7,
                  "August": 8,   "September": 9, "October": 10, "November": 11, "December": 12}
    try:
        year = timeformat.split(",")[-1].strip()
        month = timeformat.split(",")[0]
        day = timeformat.split(",")[0].split()[-1]
        newmonth = months_num[month]
        return str(newmonth)+"/"+day+"/"+year
    except:
        return ""


with open("inputDates.txt") as f:
    for y in f.readlines():
        if y.strip() != "-1":
            result = find(y.strip())
            if result != "":
                with open("parsedDates,txt", "a+") as w:
                    w.write(result+"\n")

