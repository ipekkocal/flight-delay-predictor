import pandas as pd

def load_and_preprocess_data(filepath: str) -> pd.DataFrame:
    # Load the CSV
    df = pd.read_csv(filepath)

    # Convert 'Month' column to datetime
    df['Month'] = pd.to_datetime(df['Month'])

    # Extract time-based features
    df['Year'] = df['Month'].dt.year
    df['Month_Num'] = df['Month'].dt.month

    # Drop original 'Month' column if not needed
    df = df.drop(columns=['Month'])

    # Optionally rename 'Passengers' as target
    df = df.rename(columns={'Passengers': 'Target'})

    return df
