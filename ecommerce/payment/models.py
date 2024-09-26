from django.db import models
from django.contrib.auth.models import User
from store.models import Product

class ShippingAddress(models.Model):

    nome_completo = models.CharField(max_length=300)

    email = models.CharField(max_length=300)

    endereco = models.CharField(max_length=300)

    bairro = models.CharField(max_length=300)

    cidade = models.CharField(max_length=300)

    #Opcional
    estado = models.CharField(max_length=300, null=True, blank=True)

    cep = models.CharField(max_length=300, null=True, blank=True)

    #Chave estrangeira
    #Usuários autenticados e não-autenticados
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


    class Meta:

        verbose_name_plural = 'Shipping Address'

    def __str__(self):

        return 'Shipping Address - ' + str(self.id)
    

class Order(models.Model):

    full_name = models.CharField(max_length=300)

    email = models.EmailField(max_length=255)

    shipping_address = models.TextField(max_length=10000)

    amount_paid = models.DecimalField(max_digits=8, decimal_places=2) 
    
    date_ordered = models.DateTimeField(auto_now_add=True)

    #Chave estrangeira
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):

        return 'Ordem - #' + str(self.id)


class OrderItem(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)

    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    quantity = models.PositiveBigIntegerField(default=1)

    price = models.DecimalField(max_digits=8, decimal_places=2)

    #Chave estrangeira
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):

        return 'Ordem Item - #' + str(self.id)







