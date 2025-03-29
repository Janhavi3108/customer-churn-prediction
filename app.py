from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel

# Load the trained model
model = joblib.load("customer_churn_model.pkl")

# Initialize FastAPI app
app = FastAPI()

# Define input data format
class CustomerData(BaseModel):
    tenure: float
    MonthlyCharges: float
    TotalCharges: float
    Contract_Monthly: int
    Contract_One_year: int
    Contract_Two_year: int
    PaymentMethod_Electronic_check: int
    PaymentMethod_Mailed_check: int
    # Add all necessary input features

@app.post("/predict")
def predict_churn(data: CustomerData):
    # Convert input data to DataFrame
    input_data = pd.DataFrame([data.dict()])
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Return result
    return {"churn_prediction": "Yes" if prediction[0] == 1 else "No"}
