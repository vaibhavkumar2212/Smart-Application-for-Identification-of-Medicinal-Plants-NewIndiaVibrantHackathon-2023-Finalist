import mysql.connector

mysql_cred={'host':"localhost",'user':"root",'password':"","database_name":"db_herbalsynergy"}
# MySQL server connection information
host = mysql_cred['host']
user = mysql_cred['user']
password = mysql_cred['password']
database_name = mysql_cred['database_name']

db = mysql.connector.connect(
    host=mysql_cred['host'],
    user=mysql_cred['user'],
    password=mysql_cred['password'],
    database= mysql_cred['database_name']
)


database={'english':"herb_dtls",'hindi':"herb_dtls_hindi","gujrati":"herb_dtls_guj"}


# Function to establish the database connection
def establish_db_connection():
    try:
        db_connection = mysql.connector.connect(
            host=mysql_cred['host'],
            user=mysql_cred['user'],
            password=mysql_cred['password'],
            database= mysql_cred['database_name']
        )
        cursor = db_connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        print("database connected: ",database_name)
        return db_connection, cursor
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        print("Please connect your database.")
        return None, None
