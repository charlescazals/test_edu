
from utils.pg import get_conn


def delete_tables():
    for table in ['RAW_ONISEP_PROGRAMS', 'RAW_ONISEP_SCHOOLS', 'RAW_PARCOURSUP_PROGRAMS']:
       delete_table(table)


def delete_table(table_name):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(f"""
        DROP TABLE IF EXISTS {table_name};
    """)
    conn.commit()
    cursor.close()
    conn.close()
