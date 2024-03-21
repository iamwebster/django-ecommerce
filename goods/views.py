from django.shortcuts import render



def get_catalog(request):
    return render(request, 'goods/catalog.html')


def get_search(request):
    return render(request, 'goods/search.html')