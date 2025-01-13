# mlapp/views.py

from django.shortcuts import render
import joblib

# Load the trained model
model = joblib.load('mlapp/house_price_model.pkl')

def predict_price(request):
    if request.method == "GET":
        try:
            # Extract query parameters
            bedrooms = int(request.GET.get('bedrooms', 0))
            bathrooms = int(request.GET.get('bathrooms', 0))
            size = int(request.GET.get('size', 0))

            # Make prediction using the model
            prediction = model.predict([[bedrooms, bathrooms, size]])

            return render(request, 'mlapp/predict_form.html', {
                'predicted_price': prediction[0]
            })
        except ValueError:
            return render(request, 'mlapp/predict_form.html', {
                'error': 'Invalid input. Please provide valid numbers for bedrooms, bathrooms, and size.'
            })
