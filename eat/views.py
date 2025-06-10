from django.shortcuts import render
import pickle
import numpy as np
import os

# Load the model
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "model.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

def home(request):
    result = None
    if request.method == "POST":
        Age = request.POST.get('Age', 0)
        Sex = request.POST.get('Sex', '').upper()
        BP = request.POST.get('BP', '').upper()
        Cholesterol = request.POST.get('Cholesterol', '').upper()
        Na_to_K = request.POST.get('Na_to_K', 0)

        # Encoding inputs
        Sexa = 0 if Sex == "M" else 1 if Sex == "F" else 0

        if BP == "LOW":
            BPa = 0
        elif BP == "NORMAL":
            BPa = 1
        elif BP == "HIGH":
            BPa = 2
        else:
            BPa = 0

        if Cholesterol == "NORMAL":
            Chola = 0
        elif Cholesterol == "HIGH":
            Chola = 1
        else:
            Chola = 0

        try:
            total = np.array([[int(Age), Sexa, BPa, Chola, float(Na_to_K)]])
            prediction = model.predict(total)
            result = prediction[0]
        except Exception as e:
            result = f"Error: {e}"

    return render(request, "home.html", {'result': result})
