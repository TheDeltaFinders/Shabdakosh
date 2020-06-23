import os
#from dotenv import load_dotenv

#load_dotenv()

DATABASE = {
    "drivername": os.getenv("DRIVERNAME", "postgresql"),
    "host": os.getenv("DB_URL", "localhost"),
    "port": os.getenv("DB_PORT", "5432"),
    "username": os.getenv("DB_USER", "prakash"),
    "database": os.getenv("DB_NAME", "shabdakosh"),
    "password": os.getenv("DB_PASSWORD",'P@ssw0rd'),
}

