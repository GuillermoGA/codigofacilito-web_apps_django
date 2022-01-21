from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from billing_profiles.models import BillingProfile


@login_required(login_url='login')
def create(request):

    if request.method == "POST":
        if request.POST.get("stripeToken"):
            if not request.user.has_customer():
                request.user.create_customer_id()

            billing_profile = BillingProfile.create_by_stripe_token(request.user, request.POST['stripeToken'])

            if billing_profile:
                messages.success(request, 'Método de pago registrado exitosamente.')

    return render(request, 'billing_profiles/create.html', {
        "stripe_public_key": settings.STRIPE_PUBLIC_KEY
    })
