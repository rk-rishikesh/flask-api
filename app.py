# from flask import Flask, request, render_template
# import joblib
# import numpy as np

# app = Flask(__name__)

# # Load the model
# model = joblib.load("xgb_model.pkl")

# # Home route
# @app.route("/")
# def home():
#     return render_template("index.html")

# # Predict route
# @app.route("/predict", methods=["POST"])
# def predict():
#     float_features = [float(request.form.get(feature)) for feature in [
#         'Engine_RPM', 'Oil_Pressure', 'Fuel_Pressure', 'Coolant_Pressure', 
#         'Oil_Temperature', 'Coolant_Temperature']]
#     features = [np.array(float_features)]
#     prediction = model.predict(features)[0]  

#     if prediction == 1:
#         prediction_text = "Engine Health is Good"
#     else:
#         prediction_text = "Engine Health is Bad"

#     return render_template("index.html", prediction_text=prediction_text)


from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_vehicle_data():
    data = {
        "data": [
            1,  # engineHealth
            3000,  # engineRPM
            55,  # fuelPressure
            90,  # coolantTemp
            30,  # coolantPressure
            100,  # oilTemp
            70  # oilPressure
        ]
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def start():
#     return "The MBSA Server is Running"

# @app.route("/mbsa")
# def mbsa():
#     return render_template('index.html')


# 
