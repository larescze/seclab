from .exploits import vulnscan
from django.shortcuts import render


def index(request):
    title = "Seclab"
    search_results = vulnscan.search()
    return render(request, 'index.html', {'title': title, 'results': search_results})