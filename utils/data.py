import mysql.connector, os
from dotenv import load_dotenv

load_dotenv("config/.env")

host = os.getenv("HOST")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
database = os.getenv("DATABASE")

def get_conn():
    try:
        return mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
    except mysql.connector.Error as e:
        print("Database-tilkoblingsfeil:", e)
        return None

if __name__ == "__main__":
    print(host, user, password, database)
