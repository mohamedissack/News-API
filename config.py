import os

class Config:

    NEWS_API_BASE_URL ='https://newsapi.org/v2/sources?language=en&apiKey=a45ed0dd525f493fba9a73353bda0b46'
    NEWS_ARTICLE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey=a45ed0dd525f493fba9a73353bda0b46'

    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')