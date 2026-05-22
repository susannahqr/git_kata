import pandas as pd
from pathlib import Path

def load_data():
    """Load the Titanic dataset from the data folder."""
    data_path = Path(__file__).resolve().parent / "data" / "titanic.csv"
    return pd.read_csv(data_path)
