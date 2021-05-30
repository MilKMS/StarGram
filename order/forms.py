from django import forms
from .models import Order
from django.contrib.auth.models import User
from contents.models import Content

class RegisterForm(forms.Form):

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    email = forms.CharField(
        error_messages={
            'required': 'Enter the Email'
        },
        label='Email'
    )
    comment = forms.Field(
        label='Comment'
    )
    product = forms.IntegerField(
        error_messages={
            'required': 'Enter the Product'
        },
        widget=forms.HiddenInput
    )

    def clean(self):
        cleaned_data = super().clean()
        product = cleaned_data.get('product')
        email = cleaned_data.get('email')
        comment = cleaned_data.get('comment')
        user = self.request.session.get('user')
        

        if product and user:
            order = Order(
                product=Content.objects.get(pk=product),
                user=User.objects.get(username=user)
            )
            order.save()
        else:
            self.product = product
            self.add_error('product', 'No Value')