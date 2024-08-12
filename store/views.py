from django.shortcuts import render
from .models import Game, product, gold, gold1

def games(request):
    return{
        'games': Game.objects.all()
    }

def all_products(request):
    products = product.objects.all()
    return render(request, 'store/home.html', {'products':products})


def retail_gold(request):
    golds = gold.objects.all()
    golds1 = gold1.objects.all()
    return render(request, 'store/retail_gold.html', {'golds':golds, 'golds1':golds1})

def contact(request):
    return render(request, "store/contact.html")
# Create your views here.
