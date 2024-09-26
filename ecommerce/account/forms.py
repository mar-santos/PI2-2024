
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput
from django.forms.widgets import TextInput
from django import forms

#Formulário de cadastro
class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']


    def __init__(self, *args, **kwargs):

        super(CreateUserForm, self).__init__(*args, **kwargs)

        #Campo de Email é obrigatório
        self.fields['email'].required = True
    

#Formulário de Login
class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())

    password = forms.CharField(widget=PasswordInput())

    

#Update formulário
class UpdateUserForm(forms.ModelForm):

    password = None

    class Meta:

        model = User

        fields = ['username', 'email']
        exclude = ['password1', 'password2']
    

    def __init__(self, *args, **kwargs):

        super(UpdateUserForm, self).__init__(*args, **kwargs)

        self.fields['email'].required = True


    #Validação do Email
    def clean_email(self):

        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():

            raise forms.ValidationError('Email inválido ou já está em uso')
        
        if len(email) >= 350:

            raise forms.ValidationError('Seu email é muito longo')
        
        return email


















