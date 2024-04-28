from django.forms import ModelForm
from .models import Product, Offer


# Create the form class.
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["title", "description", "price",]


class OfferForm(ModelForm):
    class Meta:
        model = Offer
        fields = ["offer", "comment", "payment",]
