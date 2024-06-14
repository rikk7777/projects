from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

class ParsingHostelsSpb:
    def __init__(self, url: str) -> None:
        self.url = url
        self.the_best_hostels = []
        
    # Получаем список лучших хостелов и отелей по цене хостелов    
    def get_the_best_hostels(self) -> None:
        with webdriver.Chrome() as driver:
            driver.get(self.url)
            time.sleep(3)

            names = [name.text for name in driver.find_elements(By.CLASS_NAME, 'hotel-list-item__name') if name.text]
            ratings = [float(rating.text.strip()) for rating in driver.find_elements(By.CLASS_NAME, 'rating__value')]
            walks = [walk.text for walk in driver.find_elements(By.CLASS_NAME, 'walk')]
            prices = [price.text.replace('\n', ' ') for price in driver.find_elements(By.CLASS_NAME, "hotel-list-item__right-part")][21:]
            labels = [info.text for info in driver.find_elements(By.CLASS_NAME, 'rating__label')]
            
            # С рейтингом 9 и выше и ближайшие по расположению к метро
            for i in range(len(names)):
                if float(ratings[i]) >= 9.0 and int(walks[i].split(' ')[0]) <= 10:
                    self.the_best_hostels.append((names[i], ratings[i], prices[i], walks[i], labels[i].split(' ')[0]))
                    
    # Записываем в файл csv        
    def write_csv(self):
        # Сначала записываем заголовки
        with open('hostelsSpb.csv', 'w', encoding='utf-8', newline='') as file:
            write = csv.writer(file, delimiter=';')
            write.writerow(
                ['Название хостела', 'Рейтинг', 'Информация о цене', 'Расстояние до метро в минутах', 'Количество отзывов гостей']
            )  
            
            for name, rating, price, walk, label in self.the_best_hostels:
                write.writerow([name, rating, price, walk, label]) 

url = 'https://m.101hotels.com/main/cities/sankt-peterburg/hostels'         
pars = ParsingHostelsSpb(url)
pars.get_the_best_hostels()
pars.write_csv()
    