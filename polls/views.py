from .exploits import vulnscan
from django.shortcuts import render

from .forms import SearchForm


def index(request):
    title = "Seclab"
    query = ""
    search_results = ""
    facets = []
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            facets = request.POST.getlist('facet')
            search_results = vulnscan.search(query, facets)
    else:
        form = SearchForm()
    return render(request, 'index.html',
                  {'title': title, 'form': form, 'search_query': query, 'results': search_results, 'facets': facets})
