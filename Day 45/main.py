import bs4
import requests

response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/').text
soup = bs4.BeautifulSoup(response, 'html.parser')

title = soup.find_all(name='h3',class_ = 'title')
for i in reversed(title):
    with open ('movies_list.txt','a',encoding='utf-8') as file:
        name = i.text
        file.write(f'{name} \n')
        print(i.text)
