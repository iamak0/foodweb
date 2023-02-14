from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from shop.models import *
from django.core.exceptions import ObjectDoesNotExist


def cart_details(request, tot=0, count=0, cart_items=None):
    try:
        ct = cart_list.objects.get(cart_id=c_id(request))
        ct_items = items.objects.filter(cart=ct, active=True)
        for i in ct_items:
            tot += (i.prodt.price * i.quty)
            count += i.quty
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', {'ci': ct_items, 't': tot, 'cn': count})


def c_id(request):
    ct_id = request.session.session_key
    if not ct_id:
        ct_id = request.session_create()
    return ct_id


def add_cart(request, product_id):
    prod = product.objects.get(id=product_id)
    try:
        ct = cart_list.objects.get(cart_id=c_id(request))
    except cart_list.DoesNotExist:
        ct = cart_list.objects.create(cart_id=c_id(request))
        ct.save()

    try:
        c_items = items.objects.get(prodt=prod, cart=ct)
        if c_items.quty < c_items.prodt.stock:
            c_items.quty += 1
        c_items.save()

    except items.DoesNotExist:
        c_items = items.objects.create(prodt=prod, quty=1, cart=ct)
        c_items.save()
    return redirect('cartDetails')


def min_cart(request, product_id):
    ct = cart_list.objects.get(cart_id=c_id(request))
    prodd = get_object_or_404(product, id=product_id)
    c_items = items.objects.get(prodt=prodd, cart=ct)
    if c_items.quty>1:
        c_items.quty-=1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cartDetails')


def cart_delete(request, product_id):
    ct = cart_list.objects.get(cart_id=c_id(request))
    prodd = get_object_or_404(product, id=product_id)
    c_items = items.objects.get(prodt=prodd, cart=ct)
    c_items.delete()
    return redirect('cartDetails')


