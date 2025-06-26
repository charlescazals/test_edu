
from utils.pg import get_conn

def transform_tables():
    for table_transform_file in [
        './transform/school.sql',
        './transform/program.sql'
    ]:
       run_transform(table_transform_file)


def run_transform(file_path):
    with open(file_path, 'r') as file:
        sql_query = file.read()
    sql_query = sql_query.strip()

    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql_query)
    conn.commit()
    cursor.close()
    conn.close()
