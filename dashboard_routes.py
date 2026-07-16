from flask import Blueprint, render_template
# Import the generator helper function
from graph_routes import generate_all_graphs

dashboard_bp = Blueprint('dashboard_bp', __name__)

@dashboard_bp.route('/dashboard')
def dashboard():
    # 1. Generate the latest graph images and save them to /static
    generate_all_graphs()
    
    # 2. Render the dashboard page which will read those static images
    return render_template('dashboard.html')