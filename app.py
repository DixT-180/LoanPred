from flask import Flask,request,render_template

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline
application = Flask(__name__)
app = application
##route for a home page

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            Age=request.form.get('Age'),



            Gender=request.form.get('Gender'),

            Experience=request.form.get('Experience'),

            Income = request.form.get('Income'),

            Family = request.form.get('Family'),
            CCAvg = request.form.get('CCAvg'),
            Education = request.form.get('Education'),
            Mortgage = request.form.get('Mortgage'),
            HomeOwnership = request.form.get('HomeOwnership'),


 

        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        predict_pipeline = PredictPipeline()
        results=predict_pipeline.predict(pred_df)
        print(results[0])
        if results[0] == 1:
            prediction_result = "Loan will be accepted"
        else:
            prediction_result = "Loan will not accepted"

        return render_template('home.html', results=prediction_result)
        
    

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)