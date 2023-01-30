import requests
from bs4 import BeautifulSoup
import time

DOMAIN = "https://spb.hh.ru/"
MAX_ID_RUSPROFILE = 11969382
HEADERS = {"Accept-Encoding":  "gzip, deflate, br",
"Accept-Language":  "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
"Connection":  "keep-alive",
"Cookie":  "fbb_s=1; fbb_u=1675083321; _ym_uid=1674859990825456749; _ym_d=1674859990; sessid=27d88044eb523acccb6574ea562f0942; _ym_visorc=b; _ym_isad=2",
"Host":  "www.rusprofile.ru",
"Referer":  "https://www.rusprofile.ru/",
"Sec-Fetch-Dest": "document",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-Site": "same-origin",
"Sec-Fetch-User": "?1",
"TE":"trailers",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0"}

id = 5969397
for id in range(id-5, id):

    time.sleep(3)
    result = requests.get(f"https://www.rusprofile.ru/id/{str(id)}", headers=HEADERS)


    soup = BeautifulSoup(result.text, "html.parser")

    #Название
    title = soup.title
    print(title.text + "\n")
    #ОГРН, ИНН, КПП
    ogrinn = soup.findAll("dl", class_="company-col")
    for item in ogrinn:
        a= item.text
        a = a.replace("\n", " ").strip()

        print(a)
    #Адресс
    adress = soup.findAll("address", class_="company-info__text has-copy auto-width")
    for item in adress:
        print("\n" + item.text.replace('\n', ' ').strip())
    #Информация о директоре
    dir_info = soup.findAll("div", class_="company-row hidden-parent")
    for info in dir_info:
        print(info.text)

    print("Контакты:")
    telephones = soup.findAll("a", itemprop="telephone")
    for tel in telephones:
        print(tel.text)
