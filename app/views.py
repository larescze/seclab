from django.http import HttpResponseRedirect
from .exploits import vulnscan, xss, dos, sqli
from django.shortcuts import render
from .forms import SearchForm


def index(request):
    """
    Function prepares and renders Home page
    :param request: Request for render
    :return: Return rendered page with data
    """
    title = "Home"
    query = ""
    search_results = ""
    facets = []
    chart = ""
    limit = 18
    limit_val = ""
    # Form submit (post)
    if request.method == 'POST':
        # Request search form
        form = SearchForm(request.POST)
        if form.is_valid():
            # Received data
            query = form.cleaned_data['query']
            facets = request.POST.getlist('facet')
            chart = request.POST['chart']
            # Optional input
            if request.POST['limit']:
                limit = int(request.POST['limit'])
                limit_val = limit
            # Search Shodan database with received parameters
            search_results = vulnscan.search(query, facets, limit)
    else:
        # Return empty form
        form = SearchForm()
    # Return rendered page with data
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
    """
    Function prepares and renders Exploits page
    :param request: Request for render
    :return: Return rendered page with data
    """
    # Determines whether the current visitor is a logged in user
    if request.user.is_authenticated:
        title = "Exploits"
        response = ""
        selected = ""
        # Form submit (post)
        if request.method == 'POST':
            # Cross-site scripting exploit is selected
            if request.POST.get('select-xss'):
                selected = "xss"
            # SQL Injection exploit is selected
            elif request.POST.get('select-sqli'):
                selected = "sqli"
            # DoS exploit is selected
            elif request.POST.get('select-dos'):
                selected = "dos"
            # Cross-site scripting exploit is launched
            elif request.POST.get('xss'):
                selected = "xss"
                url = request.POST['url']
                attack_type = request.POST['attack_type']
                custom_code = request.POST['custom_code']
                # Launch XSS and wait for result
                response = xss.launch(url, attack_type, custom_code)
            # DoS exploit is launched
            elif request.POST.get('dos'):
                selected = "dos"
                port = 80
                socket_limit = 200
                host = request.POST['host']
                # Optional input
                if request.POST['port']:
                    port = int(request.POST['port'])
                # Optional input
                if request.POST['socket_limit']:
                    socket_limit = int(request.POST['socket_limit'])
                is_https = request.POST['is_https']
                # Launch DoS attack and wait for result
                response = dos.launch(host, port, socket_limit, is_https)
            # SQL Injection exploit is launched
            elif request.POST.get('sqli'):
                selected = "sqli"
                url = request.POST['url']
                attack_type = request.POST['attack_type']
                custom_code = request.POST['custom_code']
                # Launch SQLi and wait for result
                response = sqli.launch(url, attack_type, custom_code)
        # Return rendered page with data
        return render(request, 'exploits.html', {'title': title, 'selected': selected, 'response': response})
    else:
        # Redirect to login if visitor is not a logged in user
        return HttpResponseRedirect('/admin/login/')
