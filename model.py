import pickle
import numpy as np

# Load the trained models and scalers
model_diabetes = pickle.load(open('diabetes_model.sav', 'rb'))
scaler_diabetes = pickle.load(open('scaler.sav', 'rb'))

model_creatinine = pickle.load(open('creatinine_model.sav', 'rb'))
scaler_creatinine = pickle.load(open('creatinine_scaler.sav', 'rb'))

model_heart = pickle.load(open('heart_model.sav', 'rb'))
scaler_heart = pickle.load(open('heart_scaler.sav', 'rb'))

model_lung = pickle.load(open('lung_model.sav', 'rb'))
scaler_lung = pickle.load(open('lung_scaler.sav', 'rb'))

model_hair = pickle.load(open('hair_loss_model.sav', 'rb'))
scaler_hair = pickle.load(open('hair_loss_scaler.sav', 'rb'))

# Load sleep health model and scaler
model_sleep = pickle.load(open('sleep_health_model.sav', 'rb'))
scaler_sleep = pickle.load(open('sleep_health_scaler.sav', 'rb'))
label_encoder_sleep = pickle.load(open('sleep_health_label_encoder.sav', 'rb'))

# Function to predict diabetes
def predict_diabetes(input_data):
    input_scaled = scaler_diabetes.transform([input_data])
    prediction = model_diabetes.predict(input_scaled)
    return "Diabetic" if prediction[0] == 1 else "Not Diabetic"

# Function to predict creatinine levels
def predict_creatinine(input_data):
    input_scaled = scaler_creatinine.transform([input_data])
    prediction = model_creatinine.predict(input_scaled)
    return "High Creatinine Level Detected!" if prediction[0] == 1 else "Creatinine Level Normal"

# Function to predict heart disease
def predict_heart(input_data):
    input_scaled = scaler_heart.transform([input_data])
    prediction = model_heart.predict(input_scaled)
    return "Heart Disease Detected!" if prediction[0] == 1 else "No Heart Disease Detected"

# Function to predict lung disease
def predict_lung(input_data):
    input_scaled = scaler_lung.transform([input_data])
    prediction = model_lung.predict(input_scaled)
    return "Lung Cancer Detected!" if prediction[0] == 1 else "No Lung Cancer Detected"

# Function to predict hair fall
def predict_hair(input_data):
    input_scaled = scaler_hair.transform([input_data])
    prediction = model_hair.predict(input_scaled)
    return "Hair fall!" if prediction[0] == 1 else "No Hair Fall"

# Function to predict sleep disorder
def predict_sleep(input_data):
    # Scale the input data for the sleep model
    input_scaled = scaler_sleep.transform([input_data])
    prediction = model_sleep.predict(input_scaled)
    prediction_label = label_encoder_sleep.inverse_transform(prediction)
    return prediction_label[0]
