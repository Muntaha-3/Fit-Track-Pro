from flask import Blueprint, render_template, request
import os
import pandas as pd
from datetime import datetime

water_intakes_bp = Blueprint('water_intakes_bp', __name__)

def save_water_to_excel(water_liters):
    """Appends the calculated water intake and current date to the Excel database."""
    db_dir = 'db'
    file_path = os.path.join(db_dir, 'water_data.xlsx')

    # 1. Make sure the 'db' folder exists
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)

    # Get today's date formatted as YYYY-MM-DD
    today = datetime.now().strftime('%Y-%m-%d')
    new_entry = pd.DataFrame([{'Date': today, 'Water': water_liters}])

    # 2. Append to existing file or create a new one
    if os.path.exists(file_path):
        try:
            df = pd.read_excel(file_path)
            # Append the new entry
            df = pd.concat([df, new_entry], ignore_index=True)
            df.to_excel(file_path, index=False)
        except Exception as e:
            print(f"Error updating Excel file: {e}")
    else:
        try:
            new_entry.to_excel(file_path, index=False)
        except Exception as e:
            print(f"Error creating Excel file: {e}")

@water_intakes_bp.route('/water-intake', methods=['GET', 'POST'])
def water_intake():
    result = None
    glasses = None
    advice = None
    message = None

    if request.method == 'POST':
        try:
            age = int(request.form.get('age', 0))
            weight = float(request.form.get('weight', 0))
            height = float(request.form.get('height', 0))
            activity = float(request.form.get('activity', 0))
            temperature = float(request.form.get('temperature', 0))
            additional_ml = float(request.form.get('additional', 0))

            # Validation
            if age <= 0 or weight <= 0 or height <= 0:
                message = "Please enter valid Age, Weight, and Height!"
            else:
                # Base formula: 35 ml per kg
                water = (weight * 35) / 1000  # Liters

                # Age adjustment
                if age < 18:
                    water -= 0.3
                elif age > 55:
                    water -= 0.2
                else:
                    water += 0.1

                # Activity & temperature
                water += activity + temperature

                # 50% of other drinks counts
                water -= (additional_ml / 1000) * 0.5

                # Safe limits
                water = max(1.5, min(5, water))

                # Glasses (250ml each)
                glasses = round(water * 4)

                # Advice
                if temperature >= 0.8:
                    advice = "Hot weather 🌞 Increase water intake and avoid dehydration."
                elif activity >= 1:
                    advice = "High activity level 🏃‍♂️ Drink water before and after exercise."
                else:
                    advice = "Good hydration keeps your energy, skin, and digestion healthy 💧"

                result = round(water, 1)

                # --- NEW: Save the result to your Excel database! ---
                save_water_to_excel(result)

        except ValueError:
            message = "Invalid input! Please enter numeric values."

    return render_template(
        'water.html',
        result=result,
        glasses=glasses,
        advice=advice,
        message=message
    )