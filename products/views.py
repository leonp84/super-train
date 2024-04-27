from django.http import HttpResponse # noqa
from django.shortcuts import render


# Create your views here.
def landing_page(request):
    return render(
        request,
        'products/index.html',
        {'coolest': 'The Javascript Jedi'},
        )
