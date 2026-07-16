from flask import Blueprint, render_template, request
from file_handler import save_exercise_to_excel
from datetime import datetime

exercise_bp = Blueprint('exercise_bp', __name__)

@exercise_bp.route("/exercise", methods=["GET", "POST"])
def exercise_tracker():
    points = 0
    rank = "Ready to move?"
    advice = "Tip: Aim for 10,000 steps to stay at the top of your game!"
    pointer_percentage = 0

    if request.method == "POST":
        try:
            steps = int(request.form.get("steps", 0))
            duration = int(request.form.get("duration", 0))
            workout_multiplier = float(request.form.get("workout_type", 1))

            if steps <= 0 or duration < 0:
                rank = "Invalid input"
                advice = "Please enter positive numbers for steps and duration."
                points = 0
                pointer_percentage = 0
            else:
                # Activity Points
                points = round((steps / 100) + (duration * workout_multiplier))

                if steps < 4000:
                    rank = "Inactive"
                    pointer_percentage = 20
                    advice = "Try to move more today! Small steps count."
                elif steps < 8000:
                    rank = "Active"
                    pointer_percentage = 60
                    advice = "Good work! You're maintaining an active lifestyle."
                else:
                    rank = "Pro Athlete"
                    pointer_percentage = 90
                    advice = "Amazing! Keep up the excellent activity!"

                # ✅ SAVE DATA TO EXCEL
                save_exercise_to_excel({
                    "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "Steps": steps,
                    "Duration (min)": duration,
                    "Workout Multiplier": workout_multiplier,
                    "Points": points,
                    "Rank": rank
                })

        except ValueError:
            rank = "Invalid input"
            advice = "Please enter valid numbers for steps and duration."
            points = 0
            pointer_percentage = 0

    return render_template(
        "exercise.html",
        points=points,
        rank=rank,
        advice=advice,
        pointer_percentage=pointer_percentage
    )
