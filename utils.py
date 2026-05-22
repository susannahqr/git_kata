import pandas as pd
from pathlib import Path

def load_data():
    """Load the Titanic dataset and return only male passengers."""
    data_path = Path(__file__).resolve().parent / "data" / "titanic.csv"
    
    df = pd.read_csv(data_path)
    
    # Filter only men
    men_df = df[df["Sex"] == "male"]
    
    return men_df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean a DataFrame by dropping missing values and normalizing categorical columns.

    Parameters:
        df (pd.DataFrame): Input DataFrame to clean.

    Returns:
        pd.DataFrame: Cleaned DataFrame with no missing values and lowercase categorical columns.
    """
    cleaned = df.dropna()
    
    categorical_columns = cleaned.select_dtypes(include=["object", "category"]).columns
    for column in categorical_columns:
        cleaned[column] = cleaned[column].astype(str).str.lower()
    
    return cleaned


