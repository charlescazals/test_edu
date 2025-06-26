import os
from dotenv import load_dotenv
import psycopg2

def get_conn():

    # Load environment variables from .env file
    load_dotenv()

    # Retrieve connection parameters from environment variables
    db_params = {
        'dbname': os.getenv('PGDATABASE'),
        'user': os.getenv('PGUSER'),
        'password': os.getenv('PGPASSWORD'),
        'host': os.getenv('PGHOST'),
        'port': os.getenv('PGPORT')
    }

    # Establish the connection
    conn = psycopg2.connect(**db_params)
    
    return conn
