from flask import Blueprint, render_template, request
from file_handler import save_calories_to_excel  # Excel saving function
from datetime import datetime

# Create the blueprint
calorie_bp = Blueprint('calorie_bp', __name__, template_folder='templates')

@calorie_bp.route("/calorie", methods=["GET", "POST"])
def calorie_calculator():
    calories = None
    message = ""

    if request.method == "POST":
        try:
            # Get form data
            age = int(request.form.get("age", 0))
            gender = request.form.get("gender", "male")
            weight = float(request.form.get("weight", 0))
            height = float(request.form.get("height", 0))
            stress = float(request.form.get("stress_level", 1.2))
            medical = request.form.get("medical_condition", "none")
            goal = request.form.get("health_goal", "maintain")
            sleep = request.form.get("sleep_duration", "7-9")

            # Validation
            if age <= 0 or weight <= 0 or height <= 0:
                message = "Please enter valid Age, Weight, and Height."
            else:
                # BMR Calculation (Mifflin-St Jeor)
                if gender == "male":
                    bmr = 10 * weight + 6.25 * height - 5 * age + 5
                else:
                    bmr = 10 * weight + 6.25 * height - 5 * age - 161

                # TDEE
                calories = bmr * stress

                # Goal Adjustment
                if goal == "loss":
                    calories -= 400
                elif goal == "gain":
                    calories += 400

                # Medical Adjustment
                if medical == "Diabetes":
                    calories -= 100
                elif medical == "Thyroid":
                    calories -= 150
                elif medical == "Heart":
                    calories -= 120

                # Sleep Impact
                if sleep == "below-5":
                    calories -= 150
                elif sleep == "5-7":
                    calories -= 50

                # Safety floor
                if calories < 1200:
                    calories = 1200

                calories = round(calories)

                # Message generation
                message = f"Your recommended daily intake is {calories} calories to {goal} your weight. "
                if medical != "none":
                    message += f"Because of {medical}, avoid extreme dieting. "
                if sleep == "below-5":
                    message += "Low sleep may slow metabolism. Improve rest for better results."
                elif sleep == "7-9":
                    message += "Excellent sleep supports healthy metabolism."

                # --- Save to Excel ---
                save_calories_to_excel({
                    "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "Age": age,
                    "Gender": gender,
                    "Weight": weight,
                    "Height": height,
                    "Stress_Level": stress,
                    "Medical_Condition": medical,
                    "Health_Goal": goal,
                    "Sleep": sleep,
                    "Calories": calories
                })

        except ValueError:
            message = "Invalid input! Please enter numbers only for age, weight, and height."

    return render_template(
        "calorie.html",
        calories=calories,
        message=message
    )
