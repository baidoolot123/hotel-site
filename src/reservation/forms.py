from django import forms 
from .models import Reservation
from django.forms import ModelForm, TextInput

class ReservationForm(forms.ModelForm):
    #name = forms.TextInput(attrs=(label=''))

    class Meta :
        model = Reservation 
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Your name:'}),
            'phone_number': TextInput(attrs={'placeholder': 'Your phone number:'}),
            'email': TextInput(attrs={'placeholder': 'Your email:'}),
            'notes': TextInput(attrs={'placeholder': 'Your comments:'})
        }
        labels = {
            'name': '',
            'phone_number': '',
            'email': '',
            'notes': '',
        }