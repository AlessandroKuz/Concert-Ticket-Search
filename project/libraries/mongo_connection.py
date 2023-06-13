import pymongo.errors
from pymongo import MongoClient
import pandas as pd


def client_connection():
    try:
        with open('../resources/connection_string.txt', 'r') as mongo_conn_string:
            connection_string = mongo_conn_string.read().strip()
            client = MongoClient(connection_string)
            client.admin.command("ping")
            return client
    except FileNotFoundError:
        raise FileNotFoundError("File 'connection_string.txt' not found!")


def database_connection(db_name: str):
    client = client_connection()
    if db_name in client.list_database_names():
        return client[db_name]
    else:
        raise pymongo.errors.OperationFailure(f"Database '{db_name}' not found!")


def collection_connection(db_name: str, collection_name: str):
    db_selected = database_connection(db_name=db_name)
    if collection_name in db_selected.list_collection_names():
        return db_selected[collection_name]
    else:
        raise pymongo.errors.OperationFailure(f"Collection '{collection_name}' not found!")


if __name__ == "__main__":
    try:
        collection = collection_connection(db_name='Esempio_db', collection_name='Macchine')
        if collection:
            item_details = collection.find()
            df_items = pd.DataFrame(item_details)

            print(df_items.head())
            print(df_items.describe())
            print(df_items.info())
    except Exception as err:
        print(f"An error occurred: {err}")
