# Fit Track Pro 🏃‍♀️🥗💧

A responsive, feature-rich web-based **Health & Fitness Tracker** developed as part of our **Programming Fundamentals (PF)** curriculum at the Department of Data Sciences, University of Engineering and Technology (UET), Lahore. 

This application consolidates key health metrics—including BMI calculation, daily calorie tracking, water intake monitoring, activity logs, meal planning, and automated progress trend visualization—into a clean, ad-free portal[cite: 1, 2].

---

## 🎓 Academic Alignment & Core Concepts Used
This project bridges the gap between backend algorithm design and interactive front-end web interfaces[cite: 1, 2]. The following core **Programming Fundamentals** concepts are implemented directly in our Flask architecture:

* **Variables & Data Types:** Storing and manipulating user-provided metrics (weight, height, age, activity levels)[cite: 2].
* **Conditional Logic:** Dynamically categorizing BMI scores, verifying hydration targets, and performing strict form inputs validation[cite: 2].
* **Modular Programming (Functions & Blueprints):** Splitting backend computations into isolated, reusable routing blueprints (e.g., `bmi_bp`, `calorie_bp`, `feedback_bp`)[cite: 2].
* **Mathematical Operations:** Automating standardized calculations such as the Harris-Benedict formula for calorie limits and metrics rounding[cite: 2].
* **File I/O & Dynamic Data Visualization:** Generating, updating, and serving real-time dynamic trend graphs using `Matplotlib` (saved in Flask's static assets).

---

## 🛠️ Tech Stack
* **Frontend:** HTML5, CSS3, JavaScript (interactive client-side verification), FontAwesome Icons[cite: 1, 2].
* **Backend:** Python 3.x, Flask Web Framework[cite: 2].
* **Libraries:** Matplotlib (Thread-safe 'Agg' backend visualization), OS, Session[cite: 2].
* **Environment & Version Control:** VS Code, Git & GitHub[cite: 1, 2].

---

## 🌟 Key Features
1. **BMI Tracker:** Computes Body Mass Index and provides instant weight category feedback[cite: 1, 2].
2. **Calorie Calculator:** Analyzes daily nutritional needs based on personal metrics and activity level[cite: 1, 2].
3. **Water Intake Tracker:** Calculates personalized daily hydration targets[cite: 1, 2].
4. **Workout Log & Meal Planner:** Keeps tabs on regular exercise and maps out dietary intake[cite: 1, 2].
5. **Dashboard Analytics:** Visualizes fitness trend lines and bar charts using dynamically generated graphs.
6. **Integrated Feedback & Thank-You Route:** A complete, validated sequential navigation pipeline.

---

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Muntaha-3/Fit-Track-Pro.git](https://github.com/Muntaha-3/Fit-Track-Pro.git)
   cd Fit-Track-Pro
