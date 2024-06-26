from django import template

from carts.models import UserCart


register = template.Library()


@register.simple_tag()
def get_user_carts(request):
    """Template tag for getting user's shopping cart"""
    if request.user.is_authenticated:
        return UserCart.objects.filter(user=request.user)
    
    if not request.session.session_key:
        request.session.create()
    return UserCart.objects.filter(session_key=request.session.session_key)