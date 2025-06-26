import sys
from delete_tables import delete_tables
from create_tables import create_tables
from ingest_tables import ingest_tables
from transform_tables import transform_tables

if __name__ == "__main__":
    user_action = sys.argv[1] if len(sys.argv) > 1 else None
    match user_action:
        case "delete":
            delete_tables()
            print("Table deleted successfully.")
        case "create":
            create_tables()
            print("Table created successfully.")
        case "ingest":
            ingest_tables()
            print("Data ingested successfully.")
        case "transform":
            transform_tables()
            print("Table transformed successfully.")
        case _:
            print("Invalid argument. Use 'delete', 'create', 'ingest' or 'transform'.")
            sys.exit(1)
