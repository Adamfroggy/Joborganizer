# Job Tracker Application
This project is a personal job tracking tool designed to manage cold outreach emails, follow-up emails, and job application statuses. It's built using Python and integrates with MongoDB for secure data storage.

# Features
Track Cold Outreach Emails: Record details of companies you’ve contacted for job opportunities.
Track Follow-up Emails: Manage the status of follow-up emails and responses from recruiters.

Track Job Applications: Store job application information such as the company, position, application date, and response status.
MongoDB Integration: Securely stores your data in a MongoDB Atlas cluster.

# Table of Contents
Technologies Used
Project Structure
Getting Started
Environment Variables
MongoDB Setup
Usage
Contributing
License
Technologies Used
Python 3.x: The core programming language used.
MongoDB Atlas: A cloud-based NoSQL database.
pymongo: Python's MongoDB driver for connecting to the database.
dotenv: Manages environment variables securely.
Flask (optional): Could be integrated if you want to turn this into a full web application.

# Project Structure
JobTracker/
│
├── app/
│   ├── __init__.py        # Initialize the application
│   ├── db.py              # Database connection and CRUD operations
│
├── .env                   # Environment variables (MongoDB credentials)
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
Getting Started
Follow these instructions to set up and run the project locally.

Prerequisites
Python 3.x: Install it from here.
MongoDB Atlas: Create a free MongoDB cluster by visiting MongoDB Atlas.
pip: Make sure you have Python's package manager installed to handle dependencies.
Installation
Clone the Repository

Clone this project to your local machine:

git clone https://github.com/your-username/JobTracker.git
cd JobTracker
Set Up a Virtual Environment

It's recommended to create a virtual environment to manage dependencies:

python -m venv venv
Activate the virtual environment:

# On macOS/Linux
source venv/bin/activate

# On Windows
venv\Scripts\activate
Install Dependencies

Install the required Python packages from requirements.txt:

pip install -r requirements.txt
Set Up Environment Variables

Create a .env file in the root directory and add your MongoDB credentials:

MONGO_USERNAME=your-mongodb-username
MONGO_PASSWORD=your-mongodb-password
DBNAME=your-database-name
MongoDB Setup

Go to MongoDB Atlas and log in.
Set up a free cluster and whitelist your IP address under Network Access.
Add your database user under Database Access.
Replace the credentials in your .env file with the ones from MongoDB Atlas.
Environment Variables
This project uses a .env file to store sensitive information like MongoDB credentials. The .env file should include:

MONGO_USERNAME=your-mongodb-username
MONGO_PASSWORD=your-mongodb-password
DBNAME=your-database-name
MongoDB Setup
Create a Database

Once you have a cluster set up in MongoDB Atlas, create a new database and collection via the Data Explorer or mongosh:

use JobTrackerDB
db.createCollection("JobTrack")
Replace "JobTrackerDB" with your actual database name, and "JobTrack" with your desired collection name.

# Usage
Database Connection
In db.py, the MongoDB connection is established using pymongo and the credentials stored in the .env file. Here's an example:

import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve MongoDB credentials from .env file
mongodb_username = os.getenv("MONGO_USERNAME")
mongodb_password = os.getenv("MONGO_PASSWORD")
db_name = os.getenv("DBNAME")

# Connect to MongoDB
client = MongoClient(f'mongodb+srv://{mongodb_username}:{mongodb_password}@cluster0.mongodb.net/{db_name}?retryWrites=true&w=majority')

# Access the database and collection
db = client[db_name]
collection = db['JobTrack']

if __name__ == '__main__':
    print("Connected to MongoDB")
    print("Collections in DB:", db.list_collection_names())
Running the Application
To run the script that connects to MongoDB:

python app/db.py
This will connect to your MongoDB cluster and list the available collections in your database.

# Adding and Querying Data
You can modify the db.py file to include functions that add and query data in the JobTrack collection. Example:

def add_job_entry(company, position, status):
    job_data = {
        "company": company,
        "position": position,
        "status": status
    }
    collection.insert_one(job_data)
    print(f"Added job application for {company}")

def get_all_jobs():
    jobs = collection.find()
    for job in jobs:
        print(job)

You can then use these functions to add job entries or query all jobs in the database.

# Contributing
Contributions are welcome! If you would like to contribute to this project, please follow these steps:

# Fork the repository.
Create a new branch.
Make your changes and test thoroughly.
Submit a pull request.

# License
This project is licensed under the MIT License. See the LICENSE file for details.