from . views import *
from . models import *

def count(request):
    items_count=0;
    if 'admin' in request.path:
        return {}
    else:
        try:
            ct=cart_list.objects.filter(cart_id=c_id(request))
            cti=items.objects.all().filter(cart=ct[:1])
            for c in cti:
                items_count+=c.quty

        except cart_list.DoesNotExist:
            items_count=0
        return dict(itc=items_count)