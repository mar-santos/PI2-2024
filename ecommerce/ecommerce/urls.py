
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    #Admin url
    path('admin/', admin.site.urls),

    #Loja url
    path('', include('store.urls')),

    #Carrinho de comprar url
    path('cart/', include('cart.urls')),

    #Account url
    path('account/', include('account.urls')),

    #Payment url
    path('payment/', include('payment.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
