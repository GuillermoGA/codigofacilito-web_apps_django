from django.shortcuts import render
from django.views.generic import ListView

from shipping_addresses.forms import ShippingAddressForm
from shipping_addresses.models import ShippingAddress


class ShippingAddressListView(ListView):
    model = ShippingAddress
    template_name = 'shipping_addresses/shipping_addresses.html'

    def get_queryset(self):
        return ShippingAddress.objects.filter(user=self.request.user).order_by('-default')


def create(request):
    form = ShippingAddressForm()

    return render(request, 'shipping_addresses/create.html', {
        "form": form
    })
