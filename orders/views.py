from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import EmptyQuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from carts.utils import destroy_cart
from carts.utils import get_or_create_cart
from orders.mails import Mail
from orders.utils import breadcrumb, destroy_order
from orders.utils import get_or_create_order
from shipping_addresses.models import ShippingAddress

class OrderListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    template_name = 'orders/orders.html'

    def get_queryset(self):
        return self.request.user.orders_completed()

@login_required(login_url='login')
def order(request):
    cart = get_or_create_cart(request)
    order = get_or_create_order(cart, request)

    return render(request, 'orders/order.html', {
        "cart": cart,
        "order": order,
        "breadcrumb": breadcrumb()
    })


@login_required(login_url='login')
def address(request):
    cart = get_or_create_cart(request)
    order = get_or_create_order(cart, request)

    shipping_address = order.get_or_set_shipping_address()
    can_choose_address = request.user.shippingaddress_set.count() > 1

    return render(request, 'orders/address.html', {
        "cart": cart,
        "order": order,
        "shipping_address": shipping_address,
        "can_choose_address": can_choose_address,
        "breadcrumb": breadcrumb(address=True)
    })


@login_required(login_url='login')
def select_address(request):
    shipping_adresses = request.user.shippingaddress_set.all()

    return render(request, 'orders/select_address.html', {
        "shipping_adresses": shipping_adresses,
        "breadcrumb": breadcrumb(address=True)
    })


@login_required(login_url='login')
def check_address(request, pk):
    cart = get_or_create_cart(request)
    order = get_or_create_order(cart, request)

    shipping_address = get_object_or_404(ShippingAddress, pk=pk)

    if request.user.id != shipping_address.user_id:
        return redirect('carts:cart')

    order.update_shipping_address(shipping_address)

    return redirect('orders:address')


@login_required(login_url='login')
def confirm(request):
    cart = get_or_create_cart(request)
    order = get_or_create_order(cart, request)

    shipping_address = order.shipping_address

    if shipping_address is None:
        return redirect('orders:address')

    return render(request, "orders/confirm.html", {
        "cart": cart,
        "order": order,
        "shipping_address": shipping_address,
        "breadcrumb": breadcrumb(address=True, confirmation=True)
    })


@login_required(login_url='login')
def cancel(request):
    cart = get_or_create_cart(request)
    order = get_or_create_order(cart, request)

    if request.user.id != order.user_id:
        return redirect('carts:cart')

    order.cancel()
    destroy_cart(request)
    destroy_order(request)

    messages.error(request, 'Orden cancelada')

    return redirect('index')


@login_required(login_url='login')
def complete(request):
    cart = get_or_create_cart(request)
    order = get_or_create_order(cart, request)

    if request.user.id != order.user_id:
        return redirect('carts:cart')

    order.complete()
    Mail.send_complete_order(order, request.user)

    destroy_cart(request)
    destroy_order(request)

    messages.success(request, 'Compra completada exitosamente')
    return redirect('index')

