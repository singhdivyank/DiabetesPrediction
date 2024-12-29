import pickle

from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

MODEL = pickle.load(file=open(file='app/classifier.pkl', mode='rb'))

# create FastAPI object
app = FastAPI()

# to allow POST API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# API operations
@app.get("/inputs")
def receive_inputs(inputs: dict = Body(...)):
    glucose, insulin, bmi, age = float(inputs.get('glucose')), float(inputs.get('insulin')), float(inputs.get('bmi')), int(inputs.get('age'))
    prediction = MODEL.predict([[glucose, insulin, bmi, age]])[0]
    return {"status": "Diabetic" if prediction else "Undiabetic"}
