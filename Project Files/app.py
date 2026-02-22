import numpy as np
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the trained model (DecisionTreeClassifier saved with pickle)
model = pickle.load(open("static/model.pkl", "rb"))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    # Get input values from the form
    type = request.form['type']
    amount = float(request.form['amount'])
    oldbalanceOrg = float(request.form['oldbalanceOrg'])
    newbalanceOrig = float(request.form['newbalanceOrig'])

    # Map transaction type to numeric value
    if type == "CASH_OUT":
        val = 1
    elif type == "PAYMENT":
        val = 2
    elif type == "CASH_IN":
        val = 3
    elif type == "TRANSFER":
        val = 4
    else:
        val = 5

    # Create input array for prediction
    input_array = np.array([[val, amount, oldbalanceOrg, newbalanceOrig]])

    # Make prediction using the loaded model
    prediction = model.predict(input_array)

    # Extract the predicted output value
    output = prediction[0]

    return render_template('index.html', prediction=output)


if __name__ == '__main__':
    app.run(debug=True)
