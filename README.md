# Fit Track Pro

A responsive, feature-rich web-based **Health & Fitness Tracker** developed as part of our **Programming Fundamentals (PF)** curriculum at the Department of Data Sciences, University of Engineering and Technology (UET), Lahore. 

This application consolidates key health metrics—including BMI calculation, daily calorie tracking, water intake monitoring, activity logs, meal planning, and automated progress trend visualization—into a clean, ad-free portal.

---

##  Academic Alignment & Core Concepts Used
This project bridges the gap between backend algorithm design and interactive front-end web interfaces. The following core **Programming Fundamentals** concepts are implemented directly in our Flask architecture:

* **Variables & Data Types:** Storing and manipulating user-provided metrics (weight, height, age, activity levels).
* **Conditional Logic:** Dynamically categorizing BMI scores, verifying hydration targets, and performing strict form inputs validation.
* **Modular Programming (Functions & Blueprints):** Splitting backend computations into isolated, reusable routing blueprints (e.g., `bmi_bp`, `calorie_bp`, `feedback_bp`).
* **Mathematical Operations:** Automating standardized calculations such as the Harris-Benedict formula for calorie limits and metrics rounding.
* **File I/O & Dynamic Data Visualization:** Generating, updating, and serving real-time dynamic trend graphs using `Matplotlib` (saved in Flask's static assets).

---

##  Tech Stack
* **Frontend:** HTML5, CSS3, JavaScript (interactive client-side verification), FontAwesome Icons.
* **Backend:** Python 3.x, Flask Web Framework.
* **Libraries:** Matplotlib (Thread-safe 'Agg' backend visualization), OS, Session.
* **Environment & Version Control:** VS Code, Git & GitHub.

---

##  Key Features
1. **BMI Tracker:** Computes Body Mass Index and provides instant weight category feedback.
2. **Calorie Calculator:** Analyzes daily nutritional needs based on personal metrics and activity level.
3. **Water Intake Tracker:** Calculates personalized daily hydration targets.
4. **Workout Log & Meal Planner:** Keeps tabs on regular exercise and maps out dietary intake.
5. **Dashboard Analytics:** Visualizes fitness trend lines and bar charts using dynamically generated graphs.
6. **Integrated Feedback & Thank-You Route:** A complete, validated sequential navigation pipeline.

---
##  How to Run Locally in VS Code

Follow these simple steps to run the application on your computer using VS Code:

### 1. Open the Project in VS Code
* Open **Visual Studio Code**.
* Click on **File** -> **Open Folder...** in the top menu.
* Select and open your main `FITNESS PROJECT` folder (the directory containing `app.py`).

### 2. Open the Built-in Terminal
* Open the terminal inside VS Code by pressing ``Ctrl + ` `` (or going to **Terminal** -> **New Terminal** in the top menu).

### 3. Install Required Libraries
Before running the app, you need to install Flask and Matplotlib. Run this command in your VS Code terminal and press **Enter**:

```bash
pip install flask matplotlib
### Step 2: Push the fix to GitHub
Once you save the file in VS Code, run these quick commands in your terminal to update your repository:

```bash
git add README.md
git commit -m "Fix README formatting and separate contributors"
git push origin main
###4. Contributor
Sidratul Muntaha(@Muntaha-3)
