import os
import pandas as pd

def ensure_db_dir():
    """Ensure that the db directory exists."""
    db_dir = 'db'
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)
    return db_dir

def save_bmi_to_excel(data):
    """Saves a single BMI entry to db/bmi_data.xlsx"""
    db_dir = ensure_db_dir()
    file_path = os.path.join(db_dir, 'bmi_data.xlsx')
    
    data_date = data["Date"].split(" ")[0]
    new_entry = pd.DataFrame([{
        'Date': data_date,
        'BMI': data['BMI'],
        'Gender': data['Gender'],
        'Weight': data['Weight'],
        'Height': data['Height'],
        'Status': data['Status']
    }])

    if os.path.exists(file_path):
        try:
            df = pd.read_excel(file_path)
            df = pd.concat([df, new_entry], ignore_index=True)
            df.to_excel(file_path, index=False)
        except Exception as e:
            print(f"Error updating BMI Excel file: {e}")
    else:
        try:
            new_entry.to_excel(file_path, index=False)
        except Exception as e:
            print(f"Error creating BMI Excel file: {e}")

def save_calories_to_excel(data):
    """Saves a single calorie calculations entry to db/calories_data.xlsx"""
    db_dir = ensure_db_dir()
    file_path = os.path.join(db_dir, 'calories_data.xlsx')
    
    data_date = data["Date"].split(" ")[0]
    new_entry = pd.DataFrame([{
        'Date': data_date,
        'Calories': data['Calories'],
        'Age': data['Age'],
        'Gender': data['Gender'],
        'Weight': data['Weight'],
        'Height': data['Height'],
        'Health_Goal': data['Health_Goal']
    }])

    if os.path.exists(file_path):
        try:
            df = pd.read_excel(file_path)
            df = pd.concat([df, new_entry], ignore_index=True)
            df.to_excel(file_path, index=False)
        except Exception as e:
            print(f"Error updating Calories Excel file: {e}")
    else:
        try:
            new_entry.to_excel(file_path, index=False)
        except Exception as e:
            print(f"Error creating Calories Excel file: {e}")

def save_exercise_to_excel(data):
    """Saves a single exercise log entry to db/exercise_data.xlsx"""
    db_dir = ensure_db_dir()
    file_path = os.path.join(db_dir, 'exercise_data.xlsx')
    
    data_date = data.get("Date", "").split(" ")[0]
    new_entry = pd.DataFrame([{
        'Date': data_date,
        'Exercise': data.get('Exercise', ''),
        'Duration': data.get('Duration', 0),
        'Calories_Burned': data.get('Calories_Burned', 0)
    }])

    if os.path.exists(file_path):
        try:
            df = pd.read_excel(file_path)
            df = pd.concat([df, new_entry], ignore_index=True)
            df.to_excel(file_path, index=False)
        except Exception as e:
            print(f"Error updating Exercise Excel file: {e}")
    else:
        try:
            new_entry.to_excel(file_path, index=False)
        except Exception as e:
            print(f"Error creating Exercise Excel file: {e}")

# --- ADDED: This fixes your current ImportError for the Meal Planner ---
def save_meal_to_excel(data):
    """Saves a single meal plan log entry to db/meal_data.xlsx"""
    db_dir = ensure_db_dir()
    file_path = os.path.join(db_dir, 'meal_data.xlsx')
    
    data_date = data.get("Date", "").split(" ")[0]
    new_entry = pd.DataFrame([{
        'Date': data_date,
        'Meal_Type': data.get('Meal_Type', ''),
        'Food_Item': data.get('Food_Item', ''),
        'Calories': data.get('Calories', 0)
    }])

    if os.path.exists(file_path):
        try:
            df = pd.read_excel(file_path)
            df = pd.concat([df, new_entry], ignore_index=True)
            df.to_excel(file_path, index=False)
        except Exception as e:
            print(f"Error updating Meal Excel file: {e}")
    else:
        try:
            new_entry.to_excel(file_path, index=False)
        except Exception as e:
            print(f"Error creating Meal Excel file: {e}")