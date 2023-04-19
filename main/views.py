from django.http import JsonResponse
from django.shortcuts import render
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer


@api_view(['GET'])
def get_bbc_news_articles(request):
    limit = request.GET.get('limit', 10)
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'sources': 'bbc-news',
        'apiKey': 'f5444cdd827a4652a1cf3ab0d2f9932d'
    }
    response = requests.get(url, params=params)
    data = response.json()
    articles_data = data.get('articles', [])
    articles = ArticleSerializer(articles_data, many=True).data
    return Response({'articles': articles})


@api_view(['GET'])
def get_tnt_news_articles(request):
    limit = request.GET.get('limit', 10)
    url = 'https://api.nytimes.com/svc/topstories/v2/arts.json?api-key=GbX57YPJ0kPNaE3WCJhSQFPyNGHmDQb8'
    response = requests.get(url)
    data = response.json()
    articles_data = data.get('results', [])[:limit]
    articles = ArticleSerializer(articles_data, many=True).data
    return Response({'articles': articles})

