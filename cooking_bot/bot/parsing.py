import requests
from bs4 import BeautifulSoup
import random

url = 'https://prostorecepty.com/'
topics = ['prostye-supy-recepty/', 'prostye-deserty-i-vypechka-recepty/', 'prostye-salaty-recepty/',
          'zavtraki-prostye-i-vkusnye-recepty/', 'zakuski-prostye-i-vkusnye-recepty/', 'prostye-napitki-recepty/',
          'prostye-zagotovki-recepty/', 'nesladkaja-vypechka-recepty/', 'prostye-vtorye-bljuda-recepty/']

items = [f'{url}' + f'{item}' for item in topics]
responses = [requests.get(item) for item in items]
soups = [BeautifulSoup(r.text, 'lxml') for r in responses]

def get_bludo(num: int) -> tuple:
    text = ''
    recepti_urls = [item['href'] for item in soups[num].find_all('a', class_='eeecvbbbbz')]
    random_url =random.choice(recepti_urls)
    r1 = requests.get(random_url)
    s1 = BeautifulSoup(r1.text, 'lxml')
    u2 = url + s1.find('img', class_='photo')['src'][1:]
    r2 = requests.get(u2)
    with open('pici.jpg', 'wb') as file:
        file.write(r2.content)
    bludo = s1.find('div', class_='textcattttt')
    text += bludo.text
    return text

