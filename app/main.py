import pickle

from fastapi import FastAPI, Body

MODEL = pickle.load(file=open(file='app/classifier.pkl', mode='rb'))

# create FastAPI object
app = FastAPI()

# API operations
@app.get("/inputs")
def receive_inputs(inputs: dict = Body(...)):
    glucose, insulin, bmi, age = float(inputs.get('glucose')), float(inputs.get('insulin')), float(inputs.get('bmi')), int(inputs.get('age'))
    prediction = MODEL.predict([[glucose, insulin, bmi, age]])[0]
    return {"status": "Diabetic" if prediction else "Undiabetic"}
