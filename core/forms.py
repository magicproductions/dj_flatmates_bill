from django import forms
from .models import Flatmate, Bill


class FlatmateForm(forms.ModelForm):
    """Class to represent a flatmate who lives in the flat and pays a share of the bill."""
    
    class Meta:
        model = Flatmate
        fields = ['name', 'days_in_house']


class BillForm(forms.ModelForm):
    """Class to represent a bill, with a total amount and period of the bill."""
    
    class Meta:
        model = Bill
        fields = ['amount', 'period']


class FlatmateBillForm(forms.Form):
    """Class to represent both classes FlatmateForm & BillForm."""
    
    flatmate_form_1 = FlatmateForm(prefix='flatmate1')
    flatmate_form_2 = FlatmateForm(prefix='flatmate2')
    bill_form = BillForm()
