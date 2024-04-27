from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, get_object_or_404
from .models import Product
from .forms import ProductForm


# Create your views here.
def landing_page(request):
    products = Product.objects.all().order_by('-id')

    if request.method == 'POST':
        product_form = ProductForm(data=request.POST)
        product_form.save()

    product_form = ProductForm
    return render(
        request,
        'products/index.html',
        {'coolest': 'The Javascript Jedi',
         'products': products,
         'product_form': product_form,
         }
    )


def about_page(request):
    return render(
        request,
        'products/about.html',
        )


def delete_item(request, id):
    queryset = Product.objects.all()
    del_product = get_object_or_404(queryset, pk=id)
    del_product.delete()
    return HttpResponseRedirect(reverse('landing_page'))
