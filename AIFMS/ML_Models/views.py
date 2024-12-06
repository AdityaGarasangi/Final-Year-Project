# views.py in ML_Models
from django.shortcuts import render
from .forms import PredictionForm  # Assuming you're using a form for the input
from .predict import (
    predict_savings_for_next_month,  # Updated function import
)  # Ensure that your predict function is correctly imported


def prediction_view(request):
    prediction = None
    if request.method == "POST":
        form = PredictionForm(request.POST)
        if form.is_valid():
            income = form.cleaned_data["income"]
            expenses = form.cleaned_data["expenses"]
            previous_savings = form.cleaned_data["previous_savings"]
            prediction = predict_savings_for_next_month(
                income, expenses, previous_savings
            )  # Updated function call
    else:
        form = PredictionForm()  # Ensure the form is initialized for GET requests

    return render(
        request,
        "ML_Models/prediction.html",
        {
            "form": form,
            "prediction": prediction,  # Pass the prediction even if it's None
        },
    )
