from django.urls import path
from . import views

urlpatterns = [
    path('bbc-news-articles/', views.get_bbc_news_articles, name='get_bbc_news_articles'),
    path('tnt-news-articles/', views.get_tnt_news_articles, name='get_tnt_news_articles'),
]