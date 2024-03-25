from .models import Product
from django.db.models import Q

def query_search(query):
    if query.isdigit() and len(query) <=5:
        return Product.objects.filter(id=int(query))
    
    keywords = [word for word in query.split() if len(word) > 2]
    if not keywords:
        return None

    query_list = Q()

    for search_word in keywords:
        query_list |= Q(name__icontains=search_word)

    return Product.objects.filter(query_list)

    
    