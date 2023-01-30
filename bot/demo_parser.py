import requests
from bs4 import BeautifulSoup

DOMAIN = "https://gazeta.spb.ru/"

def parse_main():
    result = requests.get(f"{DOMAIN}")
    soup = BeautifulSoup(result.text, "html.parser")
    news = soup.findAll("a", class_="nav-link")
    for new in news:
        link = new.get("href").replace(DOMAIN, "")
        name = new.text
        yield name, link

def parse_list(url):
    result = requests.get(f"{DOMAIN}{url}")
    soup = BeautifulSoup(result.text, "html.parser")
    news = soup.findAll("a", class_="news-item-title-wrap")
    for new in news:
        name = new.text.replace("\n", "")
        link = new.get("href")
        yield name, link

def parse_exact(url):
    result = requests.get(f"{DOMAIN}{url}")
    soup = BeautifulSoup(result.text, "html.parser")
    title = soup.title.text
    date = soup.find("a", class_="news-date").text
    news = soup.find("div", class_="post-content").text.replace("\n", "")
    author = soup.find("span", itemprop="author").text.replace("\n", "").strip()
    return f"<b>{title}</b>\n\n{date}\n{news}\n\n{author}"


if __name__ == "__main__":
    print(dict(parse_main()))
    print(dict(parse_list(url="allnews/")))
    print(parse_exact(url="2515677-glava-fns-soobshhil-o-poslableniyah-po-dolgam/"))