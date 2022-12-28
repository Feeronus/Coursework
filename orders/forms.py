from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(label="Имя",max_length=50)
    last_name = forms.CharField(label="Фамилия",max_length=50)
    email = forms.EmailField(label="Эл. почта")
    address = forms.CharField(label="Адрес",max_length=250)
    postal_code = forms.CharField(label="Почтовый индекс",max_length=20)
    city = forms.CharField(label="Город", max_length=100)
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address',
                  'postal_code', 'city']
