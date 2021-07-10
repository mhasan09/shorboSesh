from django.urls import path
from . import views
urlpatterns = [
    path('api/news', views.news_api_view.as_view(), name='news_api'),
    path('api/news/<int:pk>', views.news_api_detail_view.as_view(), name='new_api_detail'),


]