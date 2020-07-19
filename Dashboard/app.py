from flask import Flask, render_template, request 
import joblib
import pandas as pd

app = Flask(__name__)

df_selected = pd.read_csv('df_selected.csv')

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/dataset', methods=("POST", "GET"))
def dataset():
    return render_template("dataset.html",tables=[df_selected.to_html(classes='data', index = False)]
        )

@app.route("/visual",methods=("POST", "GET"))
def visual():
    return render_template('visual.html')

@app.route('/feature', methods=("POST", "GET"))
def feature():
    return render_template('feature.html')

@app.route("/predict", methods = ['POST','GET'])
def predict():
    if request.method == "POST":
        input = request.form
        prediksi = model.predict([[
            int(input['Age']), int(input['MonthlyIncome']),int(input['TotalWorkingYears']),
            int(input['DistanceFromHome']), int(input['YearsAtCompany']), int(input['PercentSalaryHike']),
            int(input['NumCompaniesWorked']), int(input['YearsWithCurrManager']),int(input['EnvironmentSatisfaction']), 
            int(input['JobSatisfaction'])
        ]])[0]
        if prediksi == 0:
            result = 'Thank you for being a good Employee. Keep up with the good work'
        else:
            result = 'It is sad that you are leaving the company. Thank you for all the hard work'
        return render_template('predict.html', data = input, pred = prediksi)
    
if __name__ == "__main__":
    model = joblib.load('modelJoblib')
    app.run(debug = True)
