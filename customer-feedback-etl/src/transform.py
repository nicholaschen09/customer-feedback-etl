import pandas as pd
from extract import extract_csv 
from transform import transform_data
from load import load_data

def main():
    raw_data = extract_csv("data/raw/customer-feedback.csv")
    if raw_data is None:
        print("Extraction failed. Exiting program.")
        return  
    
    processed_data = transform_data(raw_data)
    
    load_data(processed_data, "data/processed/processed_feedback.csv")

if __name__ == "__main__":
    main()