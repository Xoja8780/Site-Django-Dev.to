

from django.urls import path
from .views import article_search

urlpatterns = [
path('', article_search, name='search'),
]
