from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['session']
        widgets = {
            'session': forms.HiddenInput()
        }
