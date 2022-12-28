"""
Эта программа парсит цитаты известных писателей 
"""
import requests
from bs4 import BeautifulSoup
import lxml
import config
import time


for num in range(1, 380):

    if num == 1:
        req = requests.get(url=config.URL, headers=config.HEADER)
        req.encoding = 'utf-8'
        req = req.text
        with open('data/index.html', 'w', encoding='utf-8') as file:
            file.writelines(req)
            file.close()

        with open("data/index.html", 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'lxml')
            h1s = soup.find_all(id="lenta-card__text-quote-escaped")


            with open("data/quotes.txt", 'a', encoding='utf-8') as file:
                count = 1
                for quot in h1s:
                    qt = quot.getText().strip("<p>")
                    file.writelines(f"{count}.{qt}")
                    count += 1
                file.close()
            file.close()
        print("1-я страница собрана из 379")
    else:
        count += 1
        req = requests.get(url=config.URL+"/~" + str(num), headers=config.HEADER)
        req.encoding = 'utf-8'
        req = req.text
        with open(f'data/{num}index.html', 'w', encoding='utf-8') as file:
            file.writelines(req)
            file.close()

        with open(f"data/{num}index.html", 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'lxml')
            h1s = soup.find_all(id="lenta-card__text-quote-escaped")
            print(h1s)

            with open("data/quotes.txt", 'a', encoding='utf-8') as file:
                for quot in h1s:
                    qt = quot.getText().strip("<p>")
                    file.writelines(f"{count}.{qt}")
                    count += 1
                file.close()
            file.close()

        print(f'{num}-я страница собрана из 379')
        time.sleep(5)
