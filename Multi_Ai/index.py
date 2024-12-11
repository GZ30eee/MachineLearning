import pandas as pd

# Load datasets (example for diabetes)
diabetes_data = pd.read_csv('diabetes.csv')
heart_data = pd.read_csv('heart_disease.csv')
# Load other datasets similarly

# Check for missing values
print(diabetes_data.isnull().sum())

# Handle missing values if necessary (e.g., fill with mean)
diabetes_data.fillna(diabetes_data.mean(), inplace=True)

# Encode categorical variables if needed
diabetes_data['Outcome'] = diabetes_data['Outcome'].map({'Positive': 1, 'Negative': 0})
