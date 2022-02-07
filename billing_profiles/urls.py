from django.urls import path

from billing_profiles import views

app_name = "billing_profiles"

urlpatterns = [
    path("", views.BillingProfileListView.as_view(), name="billing_profiles"),
    path("nuevo", views.create, name="create"),
]
