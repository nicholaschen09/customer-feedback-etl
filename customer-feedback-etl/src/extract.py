import pandas as pd

def extract_csv(file_path):
    """Extracts data from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        if 'Tweet' not in data.columns: 
            print("Error: 'Tweet' column is missing in the CSV file.")
            return None
        return data
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return None