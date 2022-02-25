from django.shortcuts import render


def index(request):
    return render(request, 'frontend/index.html')


def index_diego(request):
    return render(request, 'triage/index_diego.html')
