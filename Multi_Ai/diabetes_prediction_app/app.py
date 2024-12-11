import pandas as pd
import streamlit as st
from model import predict_diabetes, predict_creatinine, predict_heart, predict_lung, predict_sleep

def welcome_page():
    st.markdown("<h1 style='text-align: center;'>Welcome to the Health Condition Detection App</h1>", unsafe_allow_html=True)
    title_width = st.markdown('<div style="width:100%; height:1px"></div>', unsafe_allow_html=True)

    st.markdown("""
        \n
        **Features of this Application:**
        - **Diabetes Abruption Detection:** Assess your risk of diabetes.
        - **Creatinine Level Detection:** Evaluate kidney function.
        - **Heart Disease Detection:** Check for heart disease risk.
        - **Lung Cancer Detection:** Evaluate lung health risk.
    """)

    st.markdown("""
    <style>
        .stButton>button {
            background-color: #4CAF50;  /* Green background */
            color: white;  /* White text */
            border-radius: 10px;  /* Rounded corners */
            padding: 10px 20px;  /* Adjust padding */
            font-size: 16px;  /* Font size */
            width: 100%;  /* Set width to 100% */
            border: none;  /* Remove the border */
            transition: background-color 0.3s ease;  /* Smooth transition for background color */
        }
        .stButton>button:hover {
            background-color: #45a049;  /* Darker green on hover */
            border: none;  /* No border change on hover */
            color: white;  /* Ensure text stays white */
        }
    </style>
    """, unsafe_allow_html=True)

    
    if st.button("Proceed to Detection Options"):
        st.session_state.page = "main"

    st.markdown("""        
        **Created by:** Ghanshyamsinh Zala 👨🏼‍💻✨\n
        **Purpose:** This application aims to provide users with quick assessments of their health conditions based on input data.\n
        **Special Thanks:** Prof. Jayesh Vagedia for encorging me to build this application. Thank you Sir.
    """)

def main_page():
    st.markdown("<h1 style='text-align: center;'>Health Condition Detection App</h1>", unsafe_allow_html=True)
    
    # CSS for styling the boxes
    st.markdown("""
    <style>
        .box { display: inline-block; width: 200px; height: 150px; margin: 20px; padding: 20px; text-align: center; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); transition: transform 0.2s; }
        .box:hover { transform: scale(1.05); }
        .diabetes { background-color: #ffcccb; }
        .kidney { background-color: #add8e6; }
        .heart { background-color: #90ee90; }
        .lung { background-color: #ffffcc; }
        .sleep { background-color: #f0e68c; }
    </style>
    """, unsafe_allow_html=True)

    # Create 5 columns for the buttons
    col1, col2, col3, col4 = st.columns(4)

    # Place each button in its respective column
    with col1:
        if st.button("Diabetes Abruption Detection", key="diabetes", help="Click to assess diabetes risk."):
            st.session_state.selected = "diabetes"

    with col2:
        if st.button("Creatinine Level Detection", key="creatinine", help="Click to assess kidney function."):
            st.session_state.selected = "creatinine"

    with col3:
        if st.button("Heart Disease Detection", key="heart", help="Click to assess heart disease risk."):
            st.session_state.selected = "heart"

    with col4:
        if st.button("Lung Cancer Detection", key="lung", help="Click to assess lung cancer risk."):
            st.session_state.selected = "lung"

    # with col5:
    #     if st.button("Sleep Disorder Detection", key="sleep", help="Click to assess sleep disorder risk."):
    #         st.session_state.selected = "sleep"

    # Display input fields based on selection
    if 'selected' in st.session_state:
        if st.session_state.selected == "diabetes":
            diabetes_detection()
        elif st.session_state.selected == "creatinine":
            creatinine_detection()
        elif st.session_state.selected == "heart":
            heart_disease_detection()
        elif st.session_state.selected == "lung":
            lung_detection()
        # elif st.session_state.selected == "sleep":
        #     sleep_detection()


def diabetes_detection():
    st.header("Diabetes Detection")
    
    Pregnancies = st.number_input('No. of Pregnancies:', min_value=0)
    Glucose = st.number_input('Glucose Level:', min_value=0)
    BloodPressure = st.number_input('Blood Pressure Value:', min_value=0)
    
    # Skin Thickness Input with range in help
    SkinThickness = st.number_input(
        'Skin Thickness Value (mm):', 
        min_value=0, 
        help="This value represents the thickness of a person’s skin fold, measured in millimeters. "
             "Typically, skin thickness ranges from 10 to 50 mm. If you do not know this value, you can leave it as 0 or enter an estimated value."
    )
    
    # Insulin Input with range in help
    Insulin = st.number_input(
        'Insulin Level:', 
        min_value=0, 
        help="This value represents the insulin level in your blood, measured in micro-units per milliliter (µU/mL). "
             "Normal insulin levels range from 2 to 25 µU/mL. If you do not know your insulin level, enter 0 or leave it blank."
    )
    
    # Diabetes Pedigree Function with range in help
    DiabetesPedigreeFunction = st.number_input(
        'Diabetes Pedigree Function Value:', 
        min_value=0.0, 
        max_value=2.0,
        help="This value represents your family history of diabetes. A higher value indicates a stronger family history. "
             "The typical range is from 0.0 to 2.0, where 0.0 means no family history of diabetes, and higher values represent a greater family history of diabetes. "
             "If you do not know this value, you can leave it as 0.0."
    )
    
    # BMI Section
    bmi_option = st.radio("Do you know your BMI?", ("Yes", "No"))
    if bmi_option == "Yes":
        BMI = st.number_input('Enter your BMI Value:', min_value=0.0)
    else:
        weight = st.number_input('Weight (kg):', min_value=0)
        height = st.number_input('Height (m):', min_value=0.01)
        
        if st.button('Calculate BMI'):
            if weight > 0 and height > 0:
                BMI = weight / (height ** 2)
                st.success(f"Calculated BMI: {BMI:.2f}")
            else:
                st.error("Please enter valid weight and height values.")
    
    Age = st.number_input('Age:', min_value=0)

    if st.button('Predict Diabetes'):
        input_data = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        diagnosis = predict_diabetes(input_data)
        st.success(diagnosis)


def creatinine_detection():
    st.header("Creatinine Detection")
    
    # Age Input
    Age_Creatinine = st.number_input('Age:', min_value=0)
    
    # Gender Input
    Gender_Creatinine = st.selectbox("Select Gender:", ("Male", "Female"))
    
    # Serum Creatinine Level Input with help
    Serum_Creatinine_Level = st.number_input(
        'Serum Creatinine Level (mg/dL):', 
        min_value=0.0, 
        help="This value measures the level of creatinine in your blood. "
             "Normal serum creatinine levels are typically between 0.6 to 1.2 mg/dL for adults. "
             "Values higher than this range may indicate impaired kidney function. "
             "If you do not know your serum creatinine level, you can leave it as 0 or consult your doctor."
    )
    
    # Systolic Blood Pressure Input with help
    SystolicBP_Creatinine = st.number_input(
        'Systolic Blood Pressure (mmHg):', 
        min_value=0, 
        help="This is the higher value of your blood pressure, measured in millimeters of mercury (mmHg). "
             "Normal systolic blood pressure for adults is usually below 120 mmHg. "
             "Values higher than this range may indicate hypertension (high blood pressure)."
    )
    
    # Diastolic Blood Pressure Input with help
    DiastolicBP_Creatinine = st.number_input(
        'Diastolic Blood Pressure (mmHg):', 
        min_value=0, 
        help="This is the lower value of your blood pressure, measured in millimeters of mercury (mmHg). "
             "Normal diastolic blood pressure for adults is usually below 80 mmHg. "
             "Values higher than this may indicate hypertension (high blood pressure)."
    )
    
    # Assess Kidney Function Button
    if st.button('Assess Kidney Function'):
        gender_numeric = 1 if Gender_Creatinine == "Male" else 0
        input_data_creatinine = [Age_Creatinine, gender_numeric, Serum_Creatinine_Level, SystolicBP_Creatinine, DiastolicBP_Creatinine]
        diagnosis_creatinine = predict_creatinine(input_data_creatinine)
        st.success(diagnosis_creatinine)


def heart_disease_detection():
    st.header("Heart Disease Detection")
    
    # Age Input with help text
    Age_Heart_Disease = st.number_input('Age:', min_value=0, help="Enter your age in years. Heart disease risk increases with age.")
    
    # Gender Input with help text
    Gender_Heart_Disease = st.selectbox(
        "Select Gender:", 
        ("Male", "Female"), 
        help="Select your gender. Some risk factors for heart disease may differ based on gender."
    )
    
    # Chest Pain Type Input with radio buttons
    Chest_Pain_Type = st.radio(
        "Chest Pain Type:", 
        ("Typical Angina", "Atypical Angina", "Non-anginal pain", "Asymptomatic"), 
        help="Select the type of chest pain you experienced."
    )
    
    # Resting Blood Pressure Input with help text
    Resting_BP = st.number_input(
        'Resting Blood Pressure (mmHg):', 
        min_value=0, 
        help="Enter your resting blood pressure in millimeters of mercury (mmHg). "
             "Normal levels are typically around 120/80 mmHg."
    )
    
    # Cholesterol Level Input with help text
    Cholesterol_Level = st.number_input(
        'Serum Cholesterol (mg/dL):', 
        min_value=0, 
        help="Enter your serum cholesterol level in mg/dL. "
             "Normal cholesterol levels should be below 200 mg/dL, but high levels increase heart disease risk."
    )
    
    # Fasting Blood Sugar Input with radio buttons
    Fasting_Blood_Sugar_High_120mg_dl = st.radio(
        "Fasting Blood Sugar > 120 mg/dL:", 
        ("No", "Yes"), 
        help="Select 'Yes' if your fasting blood sugar level is greater than 120 mg/dL, otherwise select 'No'."
    )
    
    # Resting ECG Result Input with radio buttons
    Resting_ECG_Result = st.radio(
        "Resting Electrocardiographic Results:", 
        ("Normal", "ST-T wave abnormality", "Left ventricular hypertrophy"), 
        help="Select the result of your resting ECG. These results help identify heart abnormalities."
    )
    
    # Max Heart Rate Achieved Input with help text
    Max_Heart_Rate_Achieved = st.number_input(
        'Maximum Heart Rate Achieved:', 
        min_value=0, 
        help="Enter the maximum heart rate you achieved during exercise testing. "
             "Higher rates are generally better, as a low maximum heart rate may indicate heart problems."
    )
    
    # Exercise Induced Angina Input with radio buttons
    Exercise_Induced_Angina = st.radio(
        "Exercise Induced Angina:", 
        ("No", "Yes"), 
        help="Select 'Yes' if you experienced angina (chest pain) during exercise, otherwise select 'No'."
    )
    
    # Oldpeak ST Depression Relative to Rest Input with help text
    Oldpeak_ST_Depression_Relative_To_Rest = st.number_input(
        'Oldpeak ST Depression:', 
        min_value=0.0, 
        help="Enter the ST depression value relative to rest during an exercise test. "
             "Higher values (greater than 1.0) can indicate potential heart disease."
    )
    
    # Slope of Peak Exercise ST Segment Input with radio buttons
    Slope_Peak_Exercise_ST_Segment_Slope_Type = st.radio(
        "Slope of Peak Exercise ST Segment:", 
        ("Upsloping", "Flat", "Downsloping"), 
        help="Select the slope of the peak exercise ST segment. A downsloping slope may indicate heart disease."
    )
    
    # Major Vessels Colored by Fluoroscopy Input with radio buttons
    Major_Vessels_Color_Fluoroscopy_Counts = st.radio(
        "Number of Major Vessels Colored by Fluoroscopy:", 
        ("None", "One", "Two", "Three"), 
        help="Select the number of major blood vessels that were colored by fluoroscopy during testing."
    )
    
    # Thalassemia Type Input with radio buttons
    Thalassemia_Type = st.radio(
        "Thalassemia Type:", 
        ("Normal", "Fixed defect", "Reversable defect"), 
        help="Select your thalassemia type. Thalassemia can affect heart disease risk."
    )

    # Predict Heart Disease Button
    if st.button('Predict Heart Disease'):
        gender_numeric_hd = 1 if Gender_Heart_Disease == "Male" else 0
        chest_pain_type_numeric = {
            "Typical Angina": 0,
            "Atypical Angina": 1,
            "Non-anginal pain": 2,
            "Asymptomatic": 3
        }[Chest_Pain_Type]
        fasting_blood_sugar_numeric = 1 if Fasting_Blood_Sugar_High_120mg_dl == "Yes" else 0
        exercise_angina_numeric = 1 if Exercise_Induced_Angina == "Yes" else 0
        slope_numeric = {
            "Upsloping": 0,
            "Flat": 1,
            "Downsloping": 2
        }[Slope_Peak_Exercise_ST_Segment_Slope_Type]
        major_vessels_numeric = {
            "None": 0,
            "One": 1,
            "Two": 2,
            "Three": 3
        }[Major_Vessels_Color_Fluoroscopy_Counts]
        thalassemia_numeric = {
            "Normal": 1,
            "Fixed defect": 2,
            "Reversable defect": 3
        }[Thalassemia_Type]
        resting_ecg_numeric = {
            "Normal": 0,
            "ST-T wave abnormality": 1,
            "Left ventricular hypertrophy": 2
        }[Resting_ECG_Result]
        
        input_data_hd = [
            Age_Heart_Disease,
            gender_numeric_hd,
            chest_pain_type_numeric,
            Resting_BP,
            Cholesterol_Level,
            fasting_blood_sugar_numeric,
            resting_ecg_numeric,
            Max_Heart_Rate_Achieved,
            exercise_angina_numeric,
            Oldpeak_ST_Depression_Relative_To_Rest,
            slope_numeric,
            major_vessels_numeric,
            thalassemia_numeric
        ]
        
        diagnosis_hd = predict_heart(input_data_hd)
        st.success(diagnosis_hd)


def lung_detection():
    st.header("Lung Cancer Detection")
    
    # Age Input with help text
    Age_Lung = st.number_input(
        'Age:', 
        min_value=0, 
        help="Enter your age. Age is a significant factor in the risk of lung cancer."
    )
    
    # Gender Input with radio buttons and help text
    Gender_Lung = st.radio(
        "Select Gender:", 
        ("Male", "Female"), 
        help="Select your gender. Lung cancer risk can differ based on gender."
    )
    
    # Air Pollution Exposure with radio buttons and help text
    Air_Pollution = st.radio(
        "Air Pollution Exposure (1=High, 0=Low):", 
        (0, 1), 
        help="Select 'High' (1) if you are exposed to high levels of air pollution, otherwise select 'Low' (0)."
    )
    
    # Alcohol Use with radio buttons and help text
    Alcohol_Use = st.radio(
        "Alcohol Use (1=Yes, 0=No):", 
        (0, 1), 
        help="Select 'Yes' (1) if you consume alcohol regularly, otherwise select 'No' (0)."
    )
    
    # Dust Allergy with radio buttons and help text
    Dust_Allergy = st.radio(
        "Dust Allergy (1=Yes, 0=No):", 
        (0, 1), 
        help="Select 'Yes' (1) if you have a dust allergy, otherwise select 'No' (0)."
    )
    
    # Occupational Hazards with radio buttons and help text
    Occupational_Hazards = st.radio(
        "Occupational Hazards (1=Yes, 0=No):", 
        (0, 1), 
        help="Select 'Yes' (1) if your work involves exposure to hazardous substances like chemicals or dust."
    )
    
    # Genetic Risk with radio buttons and help text
    Genetic_Risk = st.radio(
        "Genetic Risk (1=Yes, 0=No):", 
        (0, 1), 
        help="Select 'Yes' (1) if you have a family history of lung cancer or genetic risk factors."
    )
    
    # Chronic Lung Disease with radio buttons and help text
    Chronic_Lung_Disease = st.radio(
        "Chronic Lung Disease (1=Yes, 0=No):", 
        (0, 1), 
        help="Select 'Yes' (1) if you have a history of chronic lung diseases such as COPD or asthma."
    )
    
    # Balanced Diet with radio buttons and help text
    Balanced_Diet = st.radio(
        "Balanced Diet (1=Yes, 0=No):", 
        (0, 1), 
        help="Select 'Yes' (1) if you maintain a healthy and balanced diet, otherwise select 'No' (0)."
    )
    
    # Obesity with radio buttons and help text
    Obesity = st.radio(
        "Obesity (1=Yes, 0=No):", 
        (0, 1), 
        help="Select 'Yes' (1) if you are obese (BMI > 30), otherwise select 'No' (0)."
    )
    
    # Smoking with radio buttons and help text
    Smoking = st.radio(
        "Smoking (1=Yes, 0=No):", 
        (0, 1), 
        help="Select 'Yes' (1) if you are a smoker, otherwise select 'No' (0). Smoking is a major risk factor for lung cancer."
    )
    
    # Passive Smoking with radio buttons and help text
    Passive_Smoker = st.radio(
        "Passive Smoking (1=Yes, 0=No):", 
        (0, 1), 
        help="Select 'Yes' (1) if you are regularly exposed to secondhand smoke, otherwise select 'No' (0)."
    )

    # Button to trigger lung cancer risk assessment
    if st.button('Assess Lung Cancer Risk'):
        # Convert categorical data into numerical values
        gender_numeric_ld = 1 if Gender_Lung == "Male" else 0
        
        input_data_ld = [
            Age_Lung, gender_numeric_ld, Air_Pollution, Alcohol_Use, Dust_Allergy,
            Occupational_Hazards, Genetic_Risk, Chronic_Lung_Disease, Balanced_Diet, Obesity, Smoking, Passive_Smoker
        ]
        
        # Get the prediction from the model
        diagnosis_ld = predict_lung(input_data_ld)
        
        # Show the prediction result
        st.success(diagnosis_ld)

def sleep_detection():
    st.header("Sleep Disorder Detection")
    
    # User input fields
    Age_Sleep = st.number_input('Age:', min_value=0)
    Gender_Sleep = st.radio("Select Gender:", ("Male", "Female"))
    Snoring = st.radio("Snoring (1=Yes, 0=No):", (0, 1))
    Excessive_Tiredness = st.radio("Excessive Tiredness (1=Yes, 0=No):", (0, 1))
    Restlessness = st.radio("Restlessness (1=Yes, 0=No):", (0, 1))
    Difficulty_Falling_Asleep = st.radio("Difficulty Falling Asleep (1=Yes, 0=No):", (0, 1))
    Morning_Headaches = st.radio("Morning Headaches (1=Yes, 0=No):", (0, 1))
    Breathing_Difficulties = st.radio("Breathing Difficulties During Sleep (1=Yes, 0=No):", (0, 1))
    Sleep_Duration = st.number_input('Sleep Duration (hours):', min_value=0.0)
    Physical_Activity_Level = st.slider("Physical Activity Level (1=Low, 5=High):", min_value=1, max_value=5)
    
    # Convert Gender to numeric
    Gender_Sleep = 0 if Gender_Sleep == 'Male' else 1
    
    # Collect input data into a list
    input_data = [
        Age_Sleep, Gender_Sleep, Snoring, Excessive_Tiredness, Restlessness,
        Difficulty_Falling_Asleep, Morning_Headaches, Breathing_Difficulties,
        Sleep_Duration, Physical_Activity_Level
    ]
    
    # Create a DataFrame with feature names
    feature_names = [
        'Age', 'Gender', 'Snoring', 'Excessive_Tiredness', 'Restlessness',
        'Difficulty_Falling_Asleep', 'Morning_Headaches', 'Breathing_Difficulties',
        'Sleep_Duration', 'Physical_Activity_Level'
    ]
    
    # Convert input data to a DataFrame
    input_data_df = pd.DataFrame([input_data], columns=feature_names)
    
    # Pass the DataFrame to the prediction function
    prediction = predict_sleep(input_data_df)
    
    # Display the prediction result
    if prediction == 'NaN':
        st.error("Prediction is NaN. Something went wrong.")
    else:
        st.success(f"Prediction: {prediction}")




if __name__ == "__main__":
    if 'page' not in st.session_state:
        st.session_state.page = 'welcome'

    if st.session_state.page == 'welcome':
        welcome_page()
    elif st.session_state.page == 'main':
        main_page()
