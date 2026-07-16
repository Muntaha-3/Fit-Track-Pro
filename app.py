import os
from flask import Flask

# This forces Flask to look exactly at your project's local directory
base_dir = os.path.abspath(os.path.dirname(__file__))
static_dir = os.path.join(base_dir, 'static')
template_dir = os.path.join(base_dir, 'templates')

app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)
app.secret_key = "super_secret_fitness_key"

# Registering Blueprints
from main_routes import main_bp
from auth_routes import auth_bp
from bmi_routes import bmi_bp
from calorie_routes import calorie_bp
from dashboard_routes import dashboard_bp
from exercise_routes import exercise_bp
from feedback_routes import feedback_bp
from final_report_routes import final_report_bp
from graph_routes import graph_bp
from meal_planner_routes import meal_planner_bp
from thankyou_routes import thankyou_bp
from water_intakes_routes import water_intakes_bp

app.register_blueprint(main_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(bmi_bp)
app.register_blueprint(calorie_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(exercise_bp)
app.register_blueprint(feedback_bp)
app.register_blueprint(final_report_bp)
app.register_blueprint(graph_bp)
app.register_blueprint(meal_planner_bp)
app.register_blueprint(thankyou_bp)
app.register_blueprint(water_intakes_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5000)