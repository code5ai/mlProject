from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

# Load the preprocessor (this should be a fitted preprocessor)
with open('preprocessor.pkl', 'rb') as f:
    preprocessor = pickle.load(f)

# Load the trained model (this should be a fitted model)
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    data = request.form

    # Extract and process input features
    gender = data['gender']
    ethnicity = data['ethnicity']
    parental_education = data['parental_level_of_education']
    lunch = data['lunch']
    test_prep_course = data['test_preparation_course']
    writing_score = float(data['writing_score'])
    reading_score = float(data['reading_score'])

    # Create input data frame
    input_data = pd.DataFrame([[gender, ethnicity, parental_education, lunch, test_prep_course, writing_score, reading_score]],
                          columns=['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course', 'writing score', 'reading score'])

    # Transform the input data using the preprocessor
    transformed_data = preprocessor.transform(input_data)

    # Make prediction
    prediction = model.predict(transformed_data)[0]

    # Render result
    return render_template('index.html', prediction_text=f'Predicted Marks: {prediction:.2f}')

