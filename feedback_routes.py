from flask import Blueprint, render_template, request, redirect, url_for, flash

feedback_bp = Blueprint('feedback_bp', __name__)

@feedback_bp.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("feedback")  # Correct field

        # Save feedback logic yahan add kar sakte ho
        # Example: save to DB or file
        print("Feedback submitted:", name, email, message)

        # ✅ Redirect to Thank You page instead of feedback page
        return redirect(url_for('thankyou_bp.thank_you'))

    return render_template("feedback.html")
