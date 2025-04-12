from extract import extract_csv 
from data_transform import transform_data  
from load import load_data  

def main():
    raw_data = extract_csv("../data/raw/customer-feedback.csv")
    
    if raw_data is None:
        print("Extraction failed. Exiting program.")
        return
    
    processed_data = transform_data(raw_data)
    if processed_data is None:
        print("Transformation failed. Exiting program.")
        return  
    
    load_data(processed_data, "../data/processed/processed_feedback.csv", "customer_feedback")

if __name__ == "__main__":
    main()