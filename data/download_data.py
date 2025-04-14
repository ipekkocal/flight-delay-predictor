import pandas as pd
import os

def download_and_save_data():
    url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"
    df = pd.read_csv(url)

    output_path = os.path.join(os.path.dirname(__file__), "flights.csv")
    df.to_csv(output_path, index=False)
    print(f"✅ Data downloaded and saved to: {output_path}")

if __name__ == "__main__":
    download_and_save_data()
