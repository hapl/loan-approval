# import Flask and jsonify
import flask
from flask import render_template, Flask, jsonify, request
import traceback #allows you to send error to user
import pandas as pd
import numpy as np
import pickle

#App definition
app = Flask(__name__)

#importing models  
with open('../data/classifier.pkl', 'rb') as f:
    model = pickle.load(f)

#with open('../data/model_columns.pkl', 'rb') as f:
#   model_columns = pickle.load (f)   

#webpage
@app.route('/')
def welcome():
    return "Welcome! Use this Flask App for Loans Approval Prediction"

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if flask.request.method == 'GET':
        return "Prediction page. Try using post with params to get a prediction."

    if flask.request.method == 'POST':
        try:
            json_ = request.json
            print(json_)
            query_ = pd.DataFrame(json_, index=[0])
            #query_ = pd.get_dummies(pd.DataFrame(json_))
            #query = query_.reindex(columns = model_columns, fill_value= 0)
            prediction = list(model.predict(query_))
            
            return jsonify({
                "prediction" : str(prediction)
            })
           
        except:
            return jsonify({
                    "trace": traceback.format_exc()
            }) 
    
if __name__ == "__main__":
    app.run()
