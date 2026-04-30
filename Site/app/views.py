from django.shortcuts import render
from django.views.decorators.cache import never_cache
import requests
from .forms import SearchForm
from django.conf import settings

@never_cache
def article_search(request):
    form = SearchForm(request.GET or None)
    articles = []
    query = ''

    if form.is_valid():
        query = form.cleaned_data.get('q')
        if query:
            url = 'https://dev.to/api/articles'
            params = {
                'search': query,
                'per_page': 30,
            }
            response = requests.get(url, params=params, headers={
                'api-key': settings.DEVTO_API_KEY
            })

            if response.status_code == 200:
                articles = response.json()

    context = {
        'form': form,
        'articles': articles,
        'query': query
    }

    return render(request, 'search.html', context)