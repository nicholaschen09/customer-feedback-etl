import psycopg2

try:
    connection = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="your_password",
    host="localhost",
    port="5432"
)
    print("Connection successful!")
    connection.close()
except Exception as e:
    print(f"Error: {e}")