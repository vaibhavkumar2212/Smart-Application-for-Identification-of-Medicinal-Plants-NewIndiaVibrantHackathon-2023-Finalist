import mysql.connector
from translate import Translator
import tkinter as tk

# MySQL server connection information
host = "localhost"
user = "root"
password = ""
database_name = "db_herbalsynergy_1"


# Function to establish the database connection
def establish_db_connection():
    try:
        db_connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database_name
        )
        cursor = db_connection.cursor()
        return db_connection, cursor
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        print("Please connect your database.")
        return None, None


# Function to create a table if it doesn't exist
def create_table_if_not_exists(cursor, table_name, table_schema):
    cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
    existing_tables = cursor.fetchall()

    if not existing_tables:
        create_table_query = f"CREATE TABLE {table_name} ({table_schema})"
        cursor.execute(create_table_query)
        print(f"Table '{table_name}' created successfully.")
    else:
        print(f"Table '{table_name}' already exists.")


# Function to insert data into the specified table
def insert_data(table_name, data):
    db_connection, cursor = establish_db_connection()

    if db_connection and cursor:
        insert_query = f"INSERT INTO {table_name} (common_name, scientific_name, palces_found, compounds, medicines, plant_index) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_query, data)
        db_connection.commit()
        db_connection.close()


# Function to translate text
def translate_text(text, to_language):
    translator = Translator(to_lang=to_language)
    return translator.translate(text)


# Function to handle the submit button click
def handle_submit():
    common_name = common_name_entry.get()
    scientific_name = scientific_name_entry.get()
    palces_found = palces_found_entry.get()
    compounds = compounds_entry.get()
    medicines = medicines_entry.get()
    plant_index = plant_index_entry.get()

    data = (common_name, scientific_name, palces_found, compounds, medicines, plant_index)

    insert_data(english_table, data)
    insert_data(hindi_table, (
    translate_text(common_name, "hi"), scientific_name, translate_text(palces_found, "hi"), compounds,
    translate_text(medicines, "hi"), translate_text(plant_index, "hi")))
    insert_data(gujarati_table, (
    translate_text(common_name, "gu"), scientific_name, translate_text(palces_found, "gu"), compounds,
    translate_text(medicines, "gu"), translate_text(plant_index, "gu")))

    clear_entries()
    status_label.config(text="Data inserted successfully!")


# Function to clear entry fields
def clear_entries():
    for entry in entry_fields:
        entry.delete(0, tk.END)


# Define the English, Hindi, and Gujarati table names
english_table = "herb_dtls"
hindi_table = "herb_dtls_hindi"
gujarati_table = "herb_dtls_guj"
