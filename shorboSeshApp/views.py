from django.shortcuts import render
from bs4 import BeautifulSoup
from requests_html import HTMLSession
def sorboSesh(requests):
    session = HTMLSession()
    site = 'https://www.prothomalo.com/collection/latest'
    html = session.get(site)
    soup = BeautifulSoup(html.content, "html.parser")
    connection = soup.find_all("div", {"class": "customStoryCard9-m__story-data__2qgWb"}, "href")
    for i in connection:
        print("█▒▒▒ সর্বশেষ/Just In ▒▒▒█")
        print(i.h2.text)
        try:
            print(i.span.text)
        except Exception as e:
            pass
        print("বিস্তারিত :", i.find('a')['href'])
        print(i.time.text)
        print("-" * 60)
