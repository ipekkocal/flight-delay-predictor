import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os
from src.preprocess import load_and_preprocess_data
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def train_and_save_model(data_path: str, model_path: str):
    # Load and preprocess data
    df = load_and_preprocess_data(data_path)

    # Split features and target
    X = df.drop(columns=["Target"])
    y = df["Target"]

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"✅ Model trained!")
    print(f"📉 Mean Squared Error: {mse:.2f}")
    print(f"📈 R² Score: {r2:.2f}")

    # Save model
    joblib.dump(model, model_path)
    print(f"💾 Model saved to: {model_path}")

if __name__ == "__main__":
    train_and_save_model("data/flights.csv", "models/flight_delay_model.pkl")
