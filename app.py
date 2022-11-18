from logging import debug
from flask import Flask, render_template, request 
import utils  
from utils import preprocessdata 
from constants import features

app = Flask(__name__) 

@app.route('/') 
def home(): 
    return render_template('index.html', features=features) 

@app.route('/predict/', methods=['POST'])
def predict(): 
        
    features = request.form.to_dict()
    for k, v in features.items():
        features[k] = float(v)

    prediction = utils.preprocessdata(features)

    return render_template('predict.html', prediction=prediction) 

if __name__ == '__main__': 
    app.run(debug=True) 
