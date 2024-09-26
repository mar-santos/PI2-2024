
from django.urls import path
from . import views

urlpatterns = [

    #Página principal
    path('', views.store, name='store'),

    #Página individual do produto
    path('product/<slug:product_slug>/', views.product_info, name='product-info'),

    #Página dos produtos por categoria
    path('search/<slug:category_slug>/', views.list_category, name='list-category'),
]



















