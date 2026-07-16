from flask import Blueprint, render_template, request
from file_handler import save_bmi_to_excel  # import the function
from datetime import datetime  # <-- import datetime here

bmi_bp = Blueprint('bmi_bp', __name__)

default_bmi_data = [22, 22.2, 22.1, 22.3, 22.5, 22.4, 22.5]

@bmi_bp.route("/bmi-calculator", methods=["GET", "POST"])
def bmi_calculator():
    bmi = None
    status = ""
    advice = ""
    percentage = 0
    gender = "Male"

    if request.method == "POST":
        gender = request.form.get("gender")
        weight = request.form.get("weight")
        height = request.form.get("height")

        if weight and height:
            weight = float(weight)
            height = float(height)

            if weight > 0 and height > 0:
                height_m = height / 100
                bmi = round(weight / (height_m ** 2), 1)

                if bmi < 18.5:
                    status = "Underweight"
                    advice = "You should increase your calorie intake."
                elif bmi < 25:
                    status = "Normal"
                    advice = "Great! Maintain your healthy lifestyle."
                elif bmi < 30:
                    status = "Overweight"
                    advice = "Try regular exercise and a balanced diet."
                else:
                    status = "Obese"
                    advice = "Consult a healthcare provider for guidance."

                percentage = min(max((bmi / 40) * 100, 0), 100)

                # --- Save to Excel ---
                save_bmi_to_excel({
                    "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "Gender": gender,
                    "Weight": weight,
                    "Height": height,
                    "BMI": bmi,
                    "Status": status
                })

    return render_template(
        "bmi.html",
        bmi=bmi,
        status=status,
        advice=advice,
        percentage=percentage,
        gender=gender
    )
