from django.http import HttpResponseRedirect

from .exploits import vulnscan, xss, sqli
from django.shortcuts import render

from .forms import SearchForm


def index(request):
    title = "Home"
    query = ""
    search_results = ""
    facets = []
    chart = ""
    limit = 18
    limit_val = ""
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            facets = request.POST.getlist('facet')
            chart = request.POST['chart']
            if request.POST['limit']:
                limit = int(request.POST['limit'])
                limit_val = limit
            search_results = vulnscan.search(query, facets, limit)
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
        }
    )


def exploits(request):
    if request.user.is_authenticated:
        title = "Exploits"
        response = ""
        selected = ""
        if request.method == 'POST':
            if request.POST.get('select-xss'):
                selected = "xss"
            if request.POST.get('select-sqli'):
                selected = "sqli"
            if request.POST.get('sqli'):
                selected = "sqli"
                url = request.POST['url']
                attack_type = request.POST['attack_type']
                custom_code = request.POST['custom_code']
                response = sqli.launch(url, attack_type, custom_code)
            if request.POST.get('xss'):
                selected = "xss"
                url = request.POST['url']
                attack_type = request.POST['attack_type']
                custom_code = request.POST['custom_code']
                response = xss.launch(url, attack_type, custom_code)
        return render(request, 'exploits.html', {'title': title, 'selected': selected, 'response': response})
    else:
        return HttpResponseRedirect('/admin/login/')
