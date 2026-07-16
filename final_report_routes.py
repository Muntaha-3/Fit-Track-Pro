from flask import Blueprint, render_template, session

final_report_bp = Blueprint('final_report_bp', __name__)

@final_report_bp.route("/final-report")
def final_report():
    # Example: session ya database se data fetch
    user_data = {
        "bmi": 22.5,
        "weight": 65,
        "height": 165,
        "calories_consumed": 2000,
        "calories_burnt": 450,
        "water": 6,
        "water_goal": 8,
        "steps": 7500,
        "workout": "30 min cardio",
        "breakfast": "Oatmeal & Fruits",
        "lunch": "Grilled Chicken Salad",
        "dinner": "Vegetable Stir Fry"
    }
    return render_template("final_report.html", data=user_data)
