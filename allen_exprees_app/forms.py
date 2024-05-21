from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Shipping




class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']






class ShippingForm(forms.ModelForm):
    class Meta:
        model = Shipping
        fields = ('tracking_number','name_of_shipper', 'Recievers_name', 'product', 'Origin', 'Destination', 'weight_in_kg', 'length_in_cm', 'height_in_cm', 'width_in_cm', 'Departure_time', 'departure_date', 'pickup_date', 'status' )

    def clean_tracking_number(self):
        tracking_number = self.cleaned_data.get('tracking_number')
        if Shipping.objects.filter(tracking_number=tracking_number).exists():
            raise forms.ValidationError("This tracking number is already in use.")
        return tracking_number
    



