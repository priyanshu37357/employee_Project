from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd
from datetime import datetime
app = Flask(__name__)


model = joblib.load("Employee_model")

prediction_history =[]

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/project')
def project():
    return render_template("project.html")

@app.route('/history')
def history():
    return render_template("history.html", history=prediction_history)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':

        age = int(request.form['age'])
        gender = request.form['gender']
        department = request.form['department']
        job_title = request.form['job_title']
        experience = int(request.form['experience'])
        education = request.form['education']

        print("output>>>>>",age, gender, department, job_title, experience, education)

        input_data = pd.DataFrame([[age, gender, department, job_title, experience, education]],
                                  columns=['Age','Gender','Department','Job_Title','Experience_Years','Education_Level'])

        predicted_salary = model.predict(input_data)[0]
        print("Pridiction for model",predicted_salary)

        prediction_history.append({
        "age": age,
        "gender": gender,
        "department": department,
        "job_title": job_title,
        "experience": experience,
        "education": education,
        "predicted_salary": round(predicted_salary, 2)
        })


        return render_template("project.html", salary=round(predicted_salary, 2))


if __name__ == "__main__":
    app.run(debug=True)
