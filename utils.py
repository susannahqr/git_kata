import pandas as pd
from pathlib import Path

def load_data():
    """Load the Titanic dataset and return only male passengers."""
    data_path = Path(__file__).resolve().parent / "data" / "titanic.csv"
    
    df = pd.read_csv(data_path)
    
    # Filter only men
    men_df = df[df["Sex"] == "male"]
    
    return men_df
