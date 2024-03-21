from django.shortcuts import render
from django.http import HttpResponse


def main_page(request):
    return render(request, 'main/main_page.html')
    

def about(request):
    return render(request, 'main/about.html')