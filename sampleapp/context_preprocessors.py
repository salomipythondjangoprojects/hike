from .models import Cart


def cartmenu_(request):
    if request.user.is_authenticated:
        cartitems=Cart.objects.filter(user=request.user)
        context={
            'cartitems':cartitems
        }
    else:
        context={

        }
    return context