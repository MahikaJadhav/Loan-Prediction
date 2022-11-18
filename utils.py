import numpy as np 
import pandas as pd
import joblib 

model = joblib.load("./static/Forest.pkl") 

def preprocessdata(features):
   features = pd.DataFrame(features, index=[0])   
   prediction = model.predict(features)
   return prediction 
