from django import forms

from .models import Product, ProductType, transaction


class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields="__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Owner'].disabled=True

class TransactionForm(forms.ModelForm):
    class Meta:
        model=transaction

        exclude=['status', 'buyer','product']



