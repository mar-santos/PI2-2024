
from django import forms
from . models import ShippingAddress

class ShippingForm(forms.ModelForm):

    class Meta:

        model = ShippingAddress

        fields = ['nome_completo', 'email', 'endereco', 'bairro', 'cidade', 'estado', 'cep',]

        exclude = ['user',]

