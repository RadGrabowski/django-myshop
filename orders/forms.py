from django import forms
from localflavor.pl.forms import PLPostalCodeField
from django.utils.translation import gettext_lazy as _
from .models import Order


class OrderCreateForm(forms.ModelForm):
    postal_code = PLPostalCodeField(label=_('Postal code'))

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
