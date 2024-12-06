# forms.py in ML_Models
from django import forms


class PredictionForm(forms.Form):
    income = forms.DecimalField(label="Income", max_digits=10, decimal_places=2)
    expenses = forms.DecimalField(label="Expenses", max_digits=10, decimal_places=2)
    previous_savings = forms.DecimalField(
        label="Previous Savings", max_digits=10, decimal_places=2
    )
