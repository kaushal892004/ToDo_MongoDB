from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient, ASCENDING
from datetime import datetime
from bson.objectid import ObjectId
import os
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_caching import Cache

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', '80e357a8449a0cd8ca642f0c0cc3b9fd6a3f45b62b09321422fd896dbe6b03e1')  # Use environment variable

# Initialize login manager
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Cache configuration
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

# MongoDB connection
client = MongoClient(os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/'))
db = client["ToDoWebApp"]
tasks_collection = db["tasks"]
users_collection = db["users"]

# Ensure index on tasks for user_id to improve performance
tasks_collection.create_index([("user_id", ASCENDING)])
users_collection.create_index([("username", ASCENDING)], unique=True)

# User model
class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id) if users_collection.find_one({"_id": ObjectId(user_id)}) else None

# Home route (No async needed here)
@app.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        try:
            title = request.form.get('title')
            desc = request.form.get('Desc')

            if not title or not desc:
                return "Title and Description are required!", 400

            tasks_collection.insert_one({
                "title": title,
                "Desc": desc,
                "date_created": datetime.utcnow(),
                "status": "pending",
                "user_id": current_user.id  # Associate task with user
            })

        except Exception as e:
            return f"An error occurred: {str(e)}", 500

    alltodo = list(tasks_collection.find({"user_id": current_user.id}))  # Fetch tasks specific to the logged-in user
    return render_template('index.html', alltodo=alltodo)

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = users_collection.find_one({"username": username})

        if user and user['password'] == password:
            login_user(User(str(user['_id'])))
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password')

    return render_template('login.html')

# Logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# Update task route (No async needed here)
@app.route('/update/<task_id>', methods=['GET', 'POST'])
@login_required
def update(task_id):
    try:
        task_id = ObjectId(task_id)
        if request.method == 'POST':
            title = request.form.get('title')
            desc = request.form.get('Desc')

            if not title or not desc:
                return "Both title and description are required to update", 400

            tasks_collection.update_one(
                {"_id": task_id, "user_id": current_user.id},  # Ensure task belongs to user
                {"$set": {"title": title, "Desc": desc}}
            )
            return redirect(url_for('home'))

        task = tasks_collection.find_one({"_id": task_id, "user_id": current_user.id})
        if task:
            return render_template('update.html', ToDo=task)
        else:
            return "Task not found", 404

    except Exception as e:
        return f"An error occurred: {str(e)}", 500

# Delete task route (No async needed here)
@app.route('/delete/<task_id>', methods=['POST'])
@login_required
def delete(task_id):
    try:
        task_id = ObjectId(task_id)
        tasks_collection.delete_one({"_id": task_id, "user_id": current_user.id})
        return redirect(url_for('home'))
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

# Cached About page route
@app.route('/about')
@cache.cached(timeout=60)
def about():
    return render_template('about.html')

# Cached Features page route
@app.route('/features')
@cache.cached(timeout=60)
def features():
    return render_template('features.html')

# Home page route (secondary)
@app.route('/home')
def home_page():
    return redirect(url_for('home'))

# Register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if users_collection.find_one({"username": username}):
            flash('Username already exists')
        else:
            users_collection.insert_one({"username": username, "password": password})
            return redirect(url_for('login'))

    return render_template('register.html')

# Main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=int(os.environ.get("PORT", 5000)))
