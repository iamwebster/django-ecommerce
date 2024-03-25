# 5:47
# Шаблонный тег

from django import template 
from django.utils.http import urlencode
from goods.models import Category

register = template.Library()


@register.simple_tag()
def categories_tag(slug):
    try:
        category = Category.objects.get(slug=slug)
        category_name = category.name
    except:
        category_name = 'All'
    return category_name


@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)