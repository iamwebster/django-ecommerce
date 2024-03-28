from django import template

from carts.models import UserCart


register = template.Library()


@register.simple_tag()
def get_user_carts(request):
    if request.user.is_authenticated:
        return UserCart.objects.filter(user=request.user)