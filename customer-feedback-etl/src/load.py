from sqlalchemy import create_engine

def load_data(data, database_url, table_name):
    """
    Loads the processed data into a database or a file.

    Args:
        data (DataFrame): The processed data to load.
        database_url (str): The database connection URL or file path.
        table_name (str): The name of the table to store the data.
    """
    try:
        # Example: Save to a CSV file
        if database_url.endswith(".csv"):
            data.to_csv(database_url, index=False)
            print(f"Data successfully saved to {database_url}")
    except Exception as e:
        print(f"Error loading data: {e}")