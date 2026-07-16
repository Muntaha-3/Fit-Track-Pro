from flask import Blueprint, render_template
import pandas as pd

# --- MUST BE FIRST: Switch Matplotlib to non-interactive 'Agg' backend ---
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import os

graph_bp = Blueprint('graph_bp', __name__)

def save_plot(fig, filename):
    """Helper to save figures directly to the static folder safely"""
    static_dir = os.path.join(os.getcwd(), 'static')
    if not os.path.exists(static_dir):
        os.makedirs(static_dir)
        
    filepath = os.path.join(static_dir, filename)
    fig.savefig(filepath, format='png', bbox_inches='tight')
    plt.close(fig) # Free memory

def generate_all_graphs():
    """Generates and saves all graph images directly to /static"""
    # --- BMI Graph ---
    try:
        bmi_df = pd.read_excel('db/bmi_data.xlsx')
        fig1, ax1 = plt.subplots()
        ax1.plot(bmi_df['Date'], bmi_df['BMI'], marker='o', color='blue')
        ax1.set_title('BMI Progress')
        ax1.set_xlabel('Date')
        ax1.set_ylabel('BMI')
        save_plot(fig1, 'bmi_graph.png')
    except Exception as e:
        print(f"Error generating BMI graph: {e}")

    # --- Calories Graph ---
    try:
        cal_df = pd.read_excel('db/calories_data.xlsx')
        fig2, ax2 = plt.subplots()
        ax2.bar(cal_df['Date'], cal_df['Calories'], color='orange')
        ax2.set_title('Calories Burned')
        ax2.set_xlabel('Date')
        ax2.set_ylabel('Calories')
        save_plot(fig2, 'calories_graph.png')
    except Exception as e:
        print(f"Error generating Calories graph: {e}")

    # --- Water Intake Graph ---
    try:
        water_df = pd.read_excel('db/water_data.xlsx')
        fig3, ax3 = plt.subplots()
        ax3.plot(water_df['Date'], water_df['Water'], marker='o', color='green')
        ax3.set_title('Water Intake (Liters)')
        ax3.set_xlabel('Date')
        ax3.set_ylabel('Liters')
        save_plot(fig3, 'water_graph.png')
    except Exception as e:
        print(f"Error generating Water graph: {e}")

# (Optional) Standalone /graphs route
@graph_bp.route('/graphs')
def graphs():
    generate_all_graphs()
    return render_template('dashboard.html')