from flask import Blueprint, render_template, session, redirect, url_for

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
@main_bp.route('/index')
@main_bp.route('/home')
def home():
    if "user" in session:
        return redirect(url_for("dashboard_bp.dashboard"))
    return render_template('index.html')