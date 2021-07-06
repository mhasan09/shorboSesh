from django.shortcuts import render
from bs4 import BeautifulSoup
from rest_framework import generics
from .models import NEWS
from requests_html import HTMLSession
from shorboSeshApp.serializers import NEWS_SERIALIZERS
def sorboSesh(requests):
    session = HTMLSession()
    site = 'https://www.prothomalo.com/collection/latest'
    html = session.get(site)
    soup = BeautifulSoup(html.content, "html.parser")
    connection = soup.find_all("div", {"class": "customStoryCard9-m__story-data__2qgWb"}, "href")

    # for i in connection:
    #     temp_dict = dict()
    #     temp_dict['NEWS_TITLE'] = i.h2.text
    #     try:
    #         temp_dict['NEWS_SUBTITLE'] = i.span.text
    #     except Exception as e:
    #         pass
    #     temp_dict['NEWS_LINK'] = i.find('a')['href']
    #     temp_dict['NEWS_SOURCE'] = 'Promothom Alo'
    #     temp_dict['POST_CREATED_AT'] = i.time.text

    for i in connection:
        obj = NEWS()
        obj.NEWS_TITLE = i.h2.text
        try:
            obj.NEWS_SUBTITLE = i.span.text
        except Exception as e:
            pass
        obj.NEWS_LINK = i.find('a')['href']
        obj.NEWS_SOURCE = 'Prothom Alo'
        obj.POST_CREATED_AT = i.time.text
        obj.save()

class news_api_view(generics.ListCreateAPIView):
    queryset = NEWS.objects.all()
    serializer_class = NEWS_SERIALIZERS

class news_api_detail_view(generics.RetrieveUpdateDestroyAPIView):
    queryset = NEWS
    serializer_class = NEWS_SERIALIZERS


