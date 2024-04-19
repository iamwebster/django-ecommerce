from django import template 
from django.utils.http import urlencode
from goods.models import Category, Style

register = template.Library()


@register.simple_tag()
def style_tag(style_url, category_name):
    try:
        style = Style.objects.filter(category__name=category_name).get(url=style_url)
        style_name = style.name
    except:
        style_name = 'All'
    return style_name


@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)


@register.simple_tag()
def get_categories_tag():
    return Category.objects.all()


@register.simple_tag()
def get_style_tag(category_name):
    return Style.objects.filter(category__name=category_name)
