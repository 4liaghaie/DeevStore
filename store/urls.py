from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.all_products, name='all_products' ),
    path('retail_gold', views.retail_gold, name="Retail_gold"),
    path('contact', views.contact, name="Contact")
]
