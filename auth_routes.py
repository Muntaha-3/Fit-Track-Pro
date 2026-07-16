from flask import Blueprint, render_template, request, redirect, url_for, session

auth_bp = Blueprint("auth_bp", __name__)

# Login route
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if "user" in session:
        return redirect(url_for("dashboard_bp.dashboard"))
        
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        
        # Check session or DB here (DUMMY CHECK FOR NOW)
        if email and password:
            session["user"] = email
            return redirect(url_for("dashboard_bp.dashboard"))
        return render_template("login.html", error="Invalid credentials!")
    return render_template("login.html")


# Signup route
@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        full_name = request.form.get("full_name")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if password != confirm_password:
            return render_template("signup.html", error="Passwords do not match!")

        # Save user in session or DB
        return redirect(url_for("auth_bp.login"))

    return render_template("signup.html")


# Logout route (ADDED)
@auth_bp.route("/logout")
def logout():
    session.clear()  # Session khatam
    return redirect(url_for("main_bp.home"))  # Wapis home landing page par redirect