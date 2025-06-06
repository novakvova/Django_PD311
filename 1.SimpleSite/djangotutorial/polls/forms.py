from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="Логін", 
        widget= form.TextInput(attrs={'class': 'form-control'})
        )
    email = forms.EmailField(
        label="Електронна пошта",
        required=True,
        widget= form.TextInput(attrs={'class': 'form-control'})
        )
    first_name = forms.CharField(
        label="Ім'я",
        required=True,
        widget= form.TextInput(attrs={'class': 'form-control'})
        )
    last_name = forms.CharField(
        label="Прізвище",
        required=True,
        widget= form.TextInput(attrs={'class': 'form-control'})
        )
    image = forms.ImageField(
        label="Зображення",
        required=True,
        widget= form.FileInput(attrs={'class': 'form-control'})
        )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
        )
    password2 = forms.CharField(
        label="Повторіть пароль", 
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
        )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'image', 'password', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Ця електронна пошта вже зареєстрована")
        return email