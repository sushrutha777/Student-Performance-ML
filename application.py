from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

# Route for the landing page
@app.route('/')
def index():
    return render_template('index.html')

# Route for prediction form and result
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')

    try:
        # Collect data from form
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('reading_score')),
            writing_score=float(request.form.get('writing_score'))
        )

        # Convert input to DataFrame
        pred_df = data.get_data_as_data_frame()
        print("\nInput DataFrame:")
        print(pred_df)

        # Load pipeline and predict
        print("Before Prediction")
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        print("Prediction Complete:", results)

        # Show result
        return render_template('home.html', results=results[0])

    except Exception as e:
        print("❌ Error during prediction:", str(e))
        return render_template('home.html', results="⚠️ Prediction failed. Check logs.")

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0")
