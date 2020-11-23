from .exploits import vulnscan
from django.shortcuts import render

from .forms import SearchForm


def index(request):
    title = "Seclab"
    query = ""
    search_results = ""
    facets = []
    chart = ""
    page = 1
    limit = 18
    limit_val = ""
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            facets = request.POST.getlist('facet')
            chart = request.POST['chart']
            page = int(request.POST['page'])
            if request.POST['limit']:
                limit = int(request.POST['limit'])
                limit_val = limit
            search_results = vulnscan.search(query, facets, page, limit)
    else:
        form = SearchForm()
    return render(
        request,
        'index.html',
        {
            'title': title,
            'form': form,
            'search_query': query,
            'results': search_results,
            'facets': facets,
            'limit': limit,
            'limit_val': limit_val,
            'chart': chart,
            'page': page
        }
    )
