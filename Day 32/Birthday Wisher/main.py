import smtplib
import datetime
import random
import pandas

now = datetime.datetime.now()
month = now.month
day = now.day


data = pandas.read_csv('birthdays.csv')
info = data.to_dict(orient='records')
for i in info:
    if month == i['month'] and day == i['day']:
        with open('letter_2.txt') as file:
            letter = file.read()
            letter = letter.replace('NAME',i['name'])
            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(user='your email', password='your email app password')
                connection.sendmail(from_addr='your email',to_addrs=i['email'],msg=f"Subject:Birthday wish\n\n{letter}")
