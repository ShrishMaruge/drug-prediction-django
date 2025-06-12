# 💊 Drug Prediction using Machine Learning (Django)

A Django-based web application that predicts the most suitable drug for a patient based on their medical information. Powered by a trained machine learning model, this app demonstrates the real-world application of AI in healthcare.

---
📸 Interface Preview
Demo of prediction form:
![Screenshot 2025-06-12 215311](https://github.com/user-attachments/assets/12acb151-8f74-454b-9405-fd87aa5072cc)

---

## 🚀 Features

- 🧾 **Patient Data Form**: User-friendly form to collect:
  - Age
  - Gender (Sex)
  - Blood Pressure
  - Cholesterol
  - Sodium-to-Potassium Ratio (Na_to_K)
- 🤖 **ML Drug Prediction**: Predicts the most effective drug using a pre-trained ML model.
- 🔐 **Admin Panel**: Manage entries and oversee patient predictions with Django’s built-in admin interface.
- 📈 **Model Integration**: Seamlessly integrates a trained scikit-learn model into the Django backend.
- 🎯 **Accurate Predictions**: Based on well-curated training data and effective preprocessing.

---

## 🧠 Machine Learning Model

- **Algorithm Used**: (e.g., Decision Tree Classifier / Random Forest / Logistic Regression)  
- **Training Data**: [Include dataset source or summary if applicable]
- **Target Classes**: Drug A, Drug B, Drug C, Drug X, Drug Y (example)
- **Input Features**:
  - `Age` (Integer)
  - `Sex` (Male/Female)
  - `Blood Pressure` (Low/Normal/High)
  - `Cholesterol` (Normal/High)
  - `Na_to_K` (Float – Sodium-to-Potassium Ratio)

---

## 🖥️ Tech Stack

- **Backend**: Django (Python)
- **Machine Learning**: scikit-learn, pandas, joblib
- **Frontend**: HTML5, CSS3, Bootstrap (Optional)
- **Database**: SQLite3 (default Django DB)
- **Model Deployment**: Integrated with Django views

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/drug-prediction-django.git
cd drug-prediction-django
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Apply Migrations
```bash
python manage.py migrate
```

### 4. Run the Development Server
```bash
python manage.py runserver
```

### 5. Access the App
Open your browser and go to:  
```
http://127.0.0.1:8000/
```

---

## 🧪 Model Training (Optional for Developers)

If you want to retrain or improve the model:
```python
# train_model.py
# Uses scikit-learn to train a model and saves it as 'model.pkl' using joblib
```

---

## 📸 Screenshots

> Add screenshots of your:
- 🧾 Patient input form  
- 📈 Prediction result page  
- 🔐 Admin panel view

---

## 📁 Project Structure

```
drug-prediction/
├── core/                 # Django app
│   ├── models.py         # Patient model
│   ├── views.py          # Prediction logic
│   ├── forms.py          # Input form
│   └── templates/        # HTML templates
├── static/               # CSS/JS assets
├── model/                # Trained ML model (model.pkl)
├── train_model.py        # (Optional) Script to train and save model
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

## ✅ Example Input & Output

| Input Field           | Sample Value      |
|-----------------------|-------------------|
| Age                   | 35                |
| Gender                | Male              |
| Blood Pressure        | High              |
| Cholesterol           | High              |
| Na_to_K               | 14.2              |

**Predicted Drug**: **DrugX**

---

## 🔐 Admin Credentials

To access the admin panel:

```bash
python manage.py createsuperuser
```

Then visit:  
```
http://127.0.0.1:8000/admin
```

---

## 📜 License

MIT License. Feel free to use, modify, and distribute this project.

---

## 🙌 Acknowledgements

- scikit-learn
- Django
- UCI Drug Dataset (if applicable)
- Bootstrap (for styling)

---
