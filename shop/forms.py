# shop/forms.py
from django import forms
from .models import Trip, Option

class TripReservationForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@studbocconi.it'):
            raise forms.ValidationError("Email must be @studbocconi.it")
        return email

class TripSelectionForm(forms.Form):
    trip_id = forms.IntegerField(widget=forms.HiddenInput)
    options = forms.ModelMultipleChoiceField(
        queryset=Option.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
