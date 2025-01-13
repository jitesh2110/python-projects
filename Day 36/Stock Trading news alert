STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = "your api key of https://www.alphavantage.co"
API_KEY2 = "your api key of Use https://newsapi.org"

import requests
import datetime
import smtplib



parameters = {
    'function':'TIME_SERIES_DAILY',
    'symbol':STOCK,
    'apikey':API_KEY
}
parameters2 = {
    'q':COMPANY_NAME,
    'apiKey':API_KEY2
}
status = ''

today = datetime.datetime.now()
if today.weekday() != 5 or today.weekday() != 6:
    if today.weekday() == 0:
        yestarday = today - datetime.timedelta(days=3)
        yestarday = str(yestarday.date())

    today = str(today.date())

    responce = requests.get(url="https://www.alphavantage.co/query", params=parameters)
    responce.raise_for_status()
    stock_data = responce.json()
    print(stock_data)

    today_data = float(stock_data[today]['4. close'])
    yestarday_data = float(stock_data[yestarday]['4. close'])
    percentage = ((today_data - yestarday_data) / yestarday_data) * 100

    if percentage >5:
        status = 'increase'
    else:
        status = 'decrease'
    news = requests.get(url='https://newsapi.org/v2/everything', params=parameters2)
    news = news.json()['articles'][:3]
    new = (f"Headline:{news[0]['title']}\n Brief:{news[0]['description']}\n Headline:{news[1]['title']}\n "
           f"Brief:{news[1]['description']}\n Headline:{news[2]['title']}\n Brief:{news[2]['description']}\n")

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user='your mail', password='yor mail app password')
        connection.sendmail(from_addr='senders mail above mention mail', to_addrs='mail of a person to send to',
                            msg=f"Subject: Tesla Stocks {status} by {percentage}\n\n NEWS{new}")


