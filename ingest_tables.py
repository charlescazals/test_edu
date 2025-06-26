import csv
from utils.pg import get_conn
from utils.str import to_snakecase
from tqdm import tqdm
from psycopg2.extras import execute_values
from utils.str import to_snakecase

def ingest_tables():
    ingest_onisep_programs()
    ingest_onisep_schools()
    ingest_parcoursup_programs()

def ingest_csv_to_table(csv_path, table_name, separator=',', batch_size=1000):
    conn = get_conn()
    cur = conn.cursor()
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=separator)
        headers = next(reader)
        columns = ','.join([to_snakecase(h) for h in headers])
        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES %s"
        batch = []
        for row in tqdm(reader, desc=f"Loading {table_name}"):
            batch.append(row)
            if len(batch) >= batch_size:
                execute_values(cur, insert_query, batch)
                batch = []
        if batch:
            execute_values(cur, insert_query, batch)
    conn.commit()
    cur.close()
    conn.close()


def ingest_onisep_programs():
    ingest_csv_to_table(
        csv_path='./raw_data/onisep_programs.csv',
        table_name='RAW_ONISEP_PROGRAMS',
        separator=','
    )
def ingest_onisep_schools():
    ingest_csv_to_table(
        csv_path='./raw_data/onisep_schools.csv',
        table_name='RAW_ONISEP_SCHOOLS',
        separator=','
    )
def ingest_parcoursup_programs():
    ingest_csv_to_table(
        csv_path='./raw_data/parcoursup_programs.csv',
        table_name='RAW_PARCOURSUP_PROGRAMS',
        separator=';'
    )
