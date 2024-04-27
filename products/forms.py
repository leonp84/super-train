from django.forms import ModelForm
from .models import Product


# Create the form class.
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["title", "description", "price",]
