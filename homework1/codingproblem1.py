#Dumkele Osegi, PSID 1894081
from datetime import date




today_month = input('Enter todays month:\n')
today_day = input('Enter todays day:\n')
today_year = input('Enter todays year:\n')

birthday_month = input('Enter birthday month:\n')
birthday_day = input('Enter birthday day:\n')
birthday_year = int(input('Enter birthday year:\n'))
birthday_year = today_year - birthday_year

print('Birthday Calculator')
print('Current day:', today_day)
print('Month:', today_month)
print('Year:', today_year)
print('Birthday')
print('Month:', birthday_month)
print('Day:', birthday_day)
print('Year:', birthday_year)
print('You are', birthday_year ,'years old.')
if today_day == birthday_day:
    print('Happy Birthday!!')