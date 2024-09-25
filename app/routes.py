from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Load environment variables
load_dotenv()

# MongoDB connection setup
mongodb_username = os.getenv("MONGO_USERNAME")
mongodb_password = os.getenv("MONGO_PASSWORD")
db_name = os.getenv("DBNAME")

client = MongoClient(f'mongodb+srv://{mongodb_username}:{mongodb_password} \
                     @cluster0.mongodb.net/{db_name} \
                     ?retryWrites=true&w=majority')
db = client[db_name]
collection = db['JobTrack']


# Home route serving HTML
@app.route('/')
def index():
    return render_template('index.html')


# Route to handle form submission and add job entry
@app.route('/add_job', methods=['POST'])
def add_job():
    company = request.form.get('company')
    position = request.form.get('position')
    status = request.form.get('status')

    if company and position and status:
        collection.insert_one({
            'company': company,
            'position': position,
            'status': status
        })
        return redirect('/')
    else:
        return "Please provide all fields", 400


if __name__ == '__main__':
    app.run(debug=True)
