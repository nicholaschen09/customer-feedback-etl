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
        # Save to a PostgreSQL database
        if database_url.startswith("postgresql://"):
            engine = create_engine(database_url)
            data.to_sql(table_name, engine, if_exists='replace', index=False)
            print(f"Data successfully loaded into the table '{table_name}' in the database.")
        # Save to a CSV file
        elif database_url.endswith(".csv"):
            data.to_csv(database_url, index=False)
            print(f"Data successfully saved to {database_url}")
        else:
            print("Unsupported database URL or file format.")
    except Exception as e:
        print(f"Error loading data: {e}")