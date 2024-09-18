import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch MongoDB credentials from environment variables
mongodb_username = os.getenv("MONGO_USERNAME")
mongodb_password = os.getenv("MONGO_PASSWORD")
mongodb_cluster = os.getenv("MONGO_CLUSTER")
db_name = os.getenv("DBNAME")

# Create MongoDB client connection string
client = MongoClient
(f'mongodb+srv://{mongodb_username}:{mongodb_password}@{mongodb_cluster}/')

# Access the database and collection
db = client[db_name]
collection = db['JobTrack']

if __name__ == '__main__':
    print("Connected to the database:", db_name)
    print("Accessed collection:", collection.name)
