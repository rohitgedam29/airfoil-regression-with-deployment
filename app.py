import pickle
from flask import Flask,request,app,jsonify,render_template
import numpy as np
import pandas as pd

app = Flask(__name__)

model = pickle.load(open('model2.pkl','rb'))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    new_data = [list(data.values())]
    output = model.predict(new_data)[0]
    return jsonify(output)

@app.route('/predict',methods=['POST'])
def predict():
    #data = request.jsoon['data']
    #print(data)
    #new_data = [list(data.values())]
    #output = model.predict(new_data)[0]
    #return jsonify(output)
    if request.method == 'POST':
        return render_template('home.html')

if __name__=='__main__':
    app.run(debug=True)