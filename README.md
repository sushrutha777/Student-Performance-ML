# 🧠 Student Exam Performance Predictor

A full-stack machine learning web application to predict a student's math score based on their reading and writing scores, demographic information, and background. Built using Flask, Scikit-learn, and HTML5 with Bootstrap.

Features include: input form to collect student data (gender, ethnicity, test prep, scores, etc.), ML model pipeline to predict math score, data preprocessing using preprocessor.pkl, deployed locally via Flask, and a clean Bootstrap-based UI.

Project Structure:
project/
├── application.py             # Main Flask app
├── src/                       # Core ML pipeline and utilities
│   ├── pipeline/
│   │   └── predict_pipeline.py
│   ├── utils.py
│   └── exception.py
├── templates/                 # HTML templates
│   ├── home.html
│   └── index.html
├── artifacts/                 # Trained model and preprocessor
│   ├── model.pkl
│   └── preprocessor.pkl
├── notebook/                  # Data exploration and training notebooks
├── requirements.txt           # Python dependencies
├── setup.py                   # Project setup file
└── README.md                  # You're here

Technologies Used: Python 3.10+, Flask, Scikit-learn, Pandas, NumPy, Bootstrap 5, Pickle.

How to Run Locally:
1. Clone the repo:
   git clone https://github.com/sushrutha777/Student-Performance-ML.git
   cd student-score-predictor

2. Create and activate a virtual environment:
   python -m venv mlenv
   mlenv\Scripts\activate     (on Windows)
   OR
   source mlenv/bin/activate  (on Mac/Linux)

3. Install dependencies:
   pip install -r requirements.txt

4. (Optional) Train the model if artifacts are missing

5. Start the Flask application:
   python application.py

6. Open your browser and navigate to:
   http://127.0.0.1:5000

Sample Input:
Gender: Male
Race/Ethnicity: Group B
Parental Level of Education: Associate Degree
Lunch: Standard
Test Preparation Course: Completed
Reading Score: 85
Writing Score: 90

Prediction Output:
Predicted Math Score: 87.2

Author: Sushrutha S. Kottary  
LinkedIn: https://www.linkedin.com/in/sushrutha-s-kottary