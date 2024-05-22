from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

@app.route('/', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        form_data = {
            'gender': request.form.get('gender'),
            'ethnicity': request.form.get('ethnicity'),
            'parental_level_of_education': request.form.get('parental_level_of_education'),
            'lunch': request.form.get('lunch'),
            'test_preparation_course': request.form.get('test_preparation_course'),
            'reading_score': request.form.get('reading_score'),
            'writing_score': request.form.get('writing_score')
        }
        data = CustomData(
            gender=form_data['gender'],
            race_ethnicity=form_data['ethnicity'],
            parental_level_of_education=form_data['parental_level_of_education'],
            lunch=form_data['lunch'],
            test_preparation_course=form_data['test_preparation_course'],
            reading_score=int(form_data['reading_score']),
            writing_score=int(form_data['writing_score'])
        )
        pred_df = data.get_data_as_data_frame()
        print(pred_df)
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        if results[0]> 100:
            results[0] = 100
        elif results[0]< 0:
            results[0] = 0
        return render_template('home.html', results=round(results[0]), form_data=form_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
