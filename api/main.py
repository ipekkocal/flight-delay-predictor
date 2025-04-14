from fastapi import FastAPI, Request
from pydantic import BaseModel
from pymongo import MongoClient
from datetime import datetime
import joblib
import os
import boto3
import io

app = FastAPI()

# Load model from S3 (optional, adjust if local)
def load_model():
    s3 = boto3.client('s3')
    bucket = 'your-s3-bucket-name'
    key = 'flight_delay_model.pkl'
    response = s3.get_object(Bucket=bucket, Key=key)
    model_data = response['Body'].read()
    model = joblib.load(io.BytesIO(model_data))
    return model

model = load_model()

# ✅ MongoDB setup (use GitHub secret injected at runtime)
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGODB_URI)
db = client["flight_delay_db"]
logs_collection = db["prediction_logs"]
print("✅ MONGODB_URI:", MONGODB_URI)

# 📦 Define request schema
class FlightFeatures(BaseModel):
    feature1: float
    feature2: float
    # add all your actu