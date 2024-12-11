import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load your dataset
sleep_data = pd.read_csv('life.csv')

# Normalize column names to avoid issues with inconsistent naming
sleep_data.columns = sleep_data.columns.str.strip().str.lower().str.replace(' ', '_')

# Handle 'blood_pressure' column - split into systolic and diastolic
sleep_data[['systolic', 'diastolic']] = sleep_data['blood_pressure'].str.split('/', expand=True)

# Convert systolic and diastolic to numeric
sleep_data['systolic'] = pd.to_numeric(sleep_data['systolic'], errors='coerce')
sleep_data['diastolic'] = pd.to_numeric(sleep_data['diastolic'], errors='coerce')

# Drop the original 'blood_pressure' column as it's now split
sleep_data = sleep_data.drop(columns=['blood_pressure'])

# Select relevant features for sleep health detection
features = ['age', 'gender', 'occupation', 'sleep_duration', 'quality_of_sleep', 
            'physical_activity_level', 'stress_level', 'bmi_category', 'heart_rate', 
            'daily_steps', 'systolic', 'diastolic']
target = 'sleep_disorder'  # Target variable for classification

# Handle categorical columns with LabelEncoder (for 'gender' and 'occupation' in this case)
label_encoder_gender = LabelEncoder()
sleep_data['gender'] = label_encoder_gender.fit_transform(sleep_data['gender'])

label_encoder_occupation = LabelEncoder()
sleep_data['occupation'] = label_encoder_occupation.fit_transform(sleep_data['occupation'])

# If there are other categorical columns, encode them similarly
label_encoder_bmi_category = LabelEncoder()
sleep_data['bmi_category'] = label_encoder_bmi_category.fit_transform(sleep_data['bmi_category'])

label_encoder_quality_of_sleep = LabelEncoder()
sleep_data['quality_of_sleep'] = label_encoder_quality_of_sleep.fit_transform(sleep_data['quality_of_sleep'])

# Prepare the data
X = sleep_data[features]
y = sleep_data[target]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the model
model_sleep = RandomForestClassifier(random_state=42)
model_sleep.fit(X_train_scaled, y_train)

# Evaluate the model (optional)
accuracy = model_sleep.score(X_test_scaled, y_test)
print(f'Model Accuracy: {accuracy}')

# Save the trained model, scaler, and label encoders using `.sav` extension
with open('sleep_health_model.sav', 'wb') as model_file:
    pickle.dump(model_sleep, model_file)

with open('sleep_health_scaler.sav', 'wb') as scaler_file:
    pickle.dump(scaler, scaler_file)

with open('sleep_health_label_encoder_gender.sav', 'wb') as label_encoder_gender_file:
    pickle.dump(label_encoder_gender, label_encoder_gender_file)

with open('sleep_health_label_encoder_occupation.sav', 'wb') as label_encoder_occupation_file:
    pickle.dump(label_encoder_occupation, label_encoder_occupation_file)

with open('sleep_health_label_encoder_bmi_category.sav', 'wb') as label_encoder_bmi_category_file:
    pickle.dump(label_encoder_bmi_category, label_encoder_bmi_category_file)

with open('sleep_health_label_encoder_quality_of_sleep.sav', 'wb') as label_encoder_quality_of_sleep_file:
    pickle.dump(label_encoder_quality_of_sleep, label_encoder_quality_of_sleep_file)

print("Sleep health detection model, scaler, and label encoders saved successfully.")
