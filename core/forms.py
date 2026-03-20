from django import forms
from .models import Vehicle, Driver, Booking

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['license_no', 'status']


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['vehicle', 'start_date', 'end_date']
