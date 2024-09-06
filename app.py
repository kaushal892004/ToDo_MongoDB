from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId  # ObjectId for MongoDB ids
import os

app = Flask(__name__)
app.secret_key = '24d1c1653f982fe4556aa7121ba9a9ec5487fb8fa6e4d690'

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["ToDoWebApp"]  # Database
tasks_collection = db["tasks"]  # Collection

# Helper function to get all tasks
def get_all_tasks():
    return list(tasks_collection.find())

# Home route
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            title = request.form.get('title')
            Desc = request.form.get('Desc')

            if not title or not Desc:
                return "Title and Description are required!", 400

            tasks_collection.insert_one({
                "title": title,
                "Desc": Desc,
                "date_created": datetime.utcnow(),
                "status": "pending"
            })

        except Exception as e:
            return f"An error occurred: {str(e)}", 500

    alltodo = get_all_tasks()
    return render_template('index.html', alltodo=alltodo)

# Update task route
@app.route('/update/<task_id>', methods=['GET', 'POST'])
def update(task_id):
    try:
        # Convert task_id to ObjectId
        task_id = ObjectId(task_id)

        if request.method == 'POST':
            title = request.form.get('title')
            Desc = request.form.get('Desc')

            if not title or not Desc:
                return "Both title and description are required to update", 400

            # Update task in MongoDB
            tasks_collection.update_one(
                {"_id": task_id},
                {"$set": {"title": title, "Desc": Desc}}
            )
            return redirect(url_for('home'))  # Redirect to the homepage after update
        
        # Fetch the task to be updated
        task = tasks_collection.find_one({"_id": task_id})

        # Check if task exists
        if task:
            return render_template('update.html', ToDo=task)
        else:
            return "Task not found", 404

    except Exception as e:
        return f"An error occurred: {str(e)}", 500

# Delete task route
@app.route('/delete/<task_id>', methods=['POST'])
def delete(task_id):
    try:
        # Convert task_id to ObjectId
        task_id = ObjectId(task_id)
        
        # Delete task from MongoDB
        tasks_collection.delete_one({"_id": task_id})
        return redirect(url_for('home'))
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

# About page route
@app.route('/about')
def about():
    return render_template('about.html')

# Features page route
@app.route('/features')
def features():
    return render_template('features.html')

# Home page route (secondary)
@app.route('/home')
def home_page():
    return redirect(url_for('home'))

# Search route to check if a task exists by title

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=int(os.environ.get("PORT", 5000)))
