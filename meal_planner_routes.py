from flask import Blueprint, render_template, request, session
from datetime import datetime
from file_handler import save_meal_to_excel

meal_planner_bp = Blueprint('meal_planner_bp', __name__)

@meal_planner_bp.route("/meal-planner", methods=["GET", "POST"])
def meal_planner():
    message = None
    last_plan = None

    # Load previous meal plan from session
    if 'meal_plan' in session:
        last_plan = session['meal_plan']

    if request.method == "POST":
        breakfast = request.form.get("breakfast")
        lunch = request.form.get("lunch")
        dinner = request.form.get("dinner")

        if not breakfast or not lunch or not dinner:
            message = "Please select all meals for the day!"
        else:
            today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Save in session
            session['meal_plan'] = {
                "breakfast": breakfast,
                "lunch": lunch,
                "dinner": dinner,
                "date": today
            }

            last_plan = session['meal_plan']

            # ✅ SAVE TO EXCEL
            save_meal_to_excel({
                "Date": today,
                "Breakfast": breakfast,
                "Lunch": lunch,
                "Dinner": dinner
            })

            message = "Your meal plan has been successfully saved! 💪"

    return render_template(
        "meal.html",
        last_plan=last_plan,
        message=message
    )
