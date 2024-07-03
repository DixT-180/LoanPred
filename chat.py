import pandas as pd
import os
import pickle
from sklearn.compose import ColumnTransformer

# Define the load_object function to load saved models/preprocessors
def load_object(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)

# Paths to saved model and preprocessor
model_path = os.path.join("artifacts", "model.pkl")
preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')

# Example feature data to be transformed and predicted
data = {
    'Age': None,
    'Gender': None,
    'Experience': None,
    'Income': None,
    'Family': None,
    'CCAvg': None,
    'Education': None,
    'Mortgage': None,
    'HomeOwnership': None
}

# Function to greet the user
def greet_user():
    print("Welcome to our prediction service!")
    print("Please provide the following information:")

# Function to collect user input for each field
def collect_data():
    for key in data.keys():
        while True:
            value = input(f"Enter {key}: ")
            if key in ['Age', 'Experience', 'Family', 'Mortgage']:
                try:
                    data[key] = int(value)
                    break
                except ValueError:
                    print(f"Invalid input for {key}. Please enter an integer.")
            elif key in ['Income', 'CCAvg']:
                try:
                    data[key] = float(value)
                    break
                except ValueError:
                    print(f"Invalid input for {key}. Please enter a float.")
            elif key == 'Gender':
                value = value.upper()
                if len(value) == 1 and value in ['M', 'F','O']:
                    data[key] = value
                    break
                else:
                    print("Gender input must be a single character (M/F/O). Please re-enter this field.")
            elif key == 'Education':
                value = value.lower()
                if len(value) == 1 and value in ['a', 'b', 'm']:
                    data[key] = value
                    break
                else:
                    print("Education input must be a single character (a/b/m). Please re-enter this field.")
            else:
                data[key] = value
                break

# Function to allow user to edit incorrect data
def edit_data():
    field_to_edit = input("Enter the field you want to edit (e.g., 'Age', 'Income'): ")
    if field_to_edit in data:
        while True:
            new_value = input(f"Enter the new value for {field_to_edit}: ")
            if field_to_edit in ['Age', 'Experience', 'Family', 'Mortgage']:
                try:
                    data[field_to_edit] = int(new_value)
                    break
                except ValueError:
                    print(f"Invalid input for {field_to_edit}. Please enter an integer.")
            elif field_to_edit in ['Income', 'CCAvg']:
                try:
                    data[field_to_edit] = float(new_value)
                    break
                except ValueError:
                    print(f"Invalid input for {field_to_edit}. Please enter a float.")
            elif field_to_edit == 'Gender':
                new_value = new_value.upper()
                if len(new_value) == 1 and new_value in ['M', 'F']:
                    data[field_to_edit] = new_value
                    break
                else:
                    print("Gender input must be a single character (M/F). Please re-enter this field.")
            elif field_to_edit == 'Education':
                new_value = new_value.lower()
                if len(new_value) == 1 and new_value in ['a', 'b', 'c']:
                    data[field_to_edit] = new_value
                    break
                else:
                    print("Education input must be a single character (a/b/c). Please re-enter this field.")
            else:
                data[field_to_edit] = new_value
                break
        print("Data updated successfully!")
    else:
        print("Invalid field name. Please try again.")

# Function to check if all data fields are filled
def is_data_complete():
    for key, value in data.items():
        if value is None or value == '':
            return False
    return True

# Main function to orchestrate the chatbot and prediction
def main():
    greet_user()
    collect_data()
    
    while not is_data_complete():
        print("Data is incomplete or incorrect. Please provide missing or correct information:")
        collect_data()
    
    print("Data collected:")
    print(pd.DataFrame([data]))
    
    # Loading model and preprocessor
    print("\nLoading model and preprocessor...")
    model = load_object(model_path)
    preprocessor = load_object(preprocessor_path)
    print("Model and preprocessor loaded successfully.\n")
    
    # Transforming the data using ColumnTransformer (assuming 'preprocessor' is a ColumnTransformer object)
    features = pd.DataFrame([data])
    data_scaled = preprocessor.transform(features)
    
    # Making predictions
    preds = model.predict(data_scaled)
    if preds==[0]:
        print('loan will not get accepted')
    else:
        print('Loan will get accepted')
    
    print(f"Predictions: {preds}")

    # Offer to edit data if user desires
    while True:
        edit_choice = input("Would you like to edit any data? (yes/no): ").lower()
        if edit_choice == 'yes':
            edit_data()
            # Recalculate predictions with edited data
            features = pd.DataFrame([data])
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            print(f"Predictions after editing: {preds}")
        else:
            break
 
# Entry point of the program
if __name__ == "__main__":
    main()
