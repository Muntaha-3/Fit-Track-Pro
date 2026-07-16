# Fixed thankyou_routes.py[cite: 1]
from flask import Blueprint, render_template

thankyou_bp = Blueprint('thankyou_bp', __name__)

@thankyou_bp.route('/thank_you')
@thankyou_bp.route('/thankyou')
def thank_you():
    # Renders the templates/thank_you.html file[cite: 1]
    return render_template('thank_you.html')