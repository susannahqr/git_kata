import pandas as pd
from pathlib import Path

def load_data():
    """Load the Titanic dataset and return only male passengers."""
    data_path = Path(__file__).resolve().parent / "data" / "titanic.csv"
    
    df = pd.read_csv(data_path)
    
    # Filter only men
    men_df = df[df["sex"] == "male"]
    
    return men_df


def clean_data(df: pd.DataFrame, dropna_subset: list | None = None) -> pd.DataFrame:
    """
    Drops rows with missing values (optionally only for subset columns),
    lowercases all object/category columns, and returns the cleaned DataFrame.
    """
    cleaned = df.dropna(subset=dropna_subset).copy()
    categorical_columns = cleaned.select_dtypes(include=["object", "category"]).columns
    for col in categorical_columns:
        cleaned[col] = cleaned[col].astype(str).str.lower()
    return cleaned