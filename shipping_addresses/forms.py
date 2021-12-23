from django.forms import ModelForm

from shipping_addresses.models import ShippingAddress


class ShippingAddressForm(ModelForm):
    class Meta:
        model = ShippingAddress
        fields = [
            'line1',
            'line2',
            'city',
            'state',
            'country',
            'postal_code',
            'reference',
        ]

        labels = {
            'line1': "Calle 1",
            'line2': "Calle 2",
            'city': "Ciudad",
            'state': "Estado",
            'country': "País",
            'postal_code': "Codigo postal",
            'reference': "Referencias"
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Common style
        for field_data in self.fields.values():
            field_data.widget.attrs.update({
                "class": "form-control"
            })

        # Individual style
        self.fields["postal_code"].widget.attrs.update({
            "placeholder": "0000"
        })