from django.http import HttpResponseRedirect, HttpResponse # noqa
from django.shortcuts import render, reverse, get_object_or_404
from .models import Product, Offer
from .forms import ProductForm, OfferForm


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


def product_info_page(request, id):
    queryset = Product.objects.all()
    product = get_object_or_404(queryset, pk=id)

    if request.method == 'POST':
        offer_form = OfferForm(data=request.POST)
        if offer_form.is_valid:
            offer = offer_form.save(commit=False)
            offer.commenter = request.user
            offer.product = product
            offer.save()

    offer_form = OfferForm()
    offers = Offer.objects.all().filter(product_id=id)
    return render(
        request,
        'products/product.html',
        {'product': product,
         'offer_form': offer_form,
         'offers': offers
         }
        )
