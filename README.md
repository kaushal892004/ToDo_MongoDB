

# 📝 Flask To-Do Application  

A simple and robust To-Do application built using **Flask**, **MongoDB**, and **JWT-based authentication**. This application allows users to manage their tasks securely while maintaining user data integrity and privacy.

## 🚀 Features  

- **User Authentication**:  
  - Secure user registration and login using **JWT (JSON Web Tokens)**.  
  - Passwords stored securely with **bcrypt hashing**.  
- **Task Management**:  
  - Add, edit, delete, and mark tasks as complete.  
  - Tasks are personalized for each user.  
- **Database Integration**:  
  - All data is stored in **MongoDB**, ensuring scalability and performance.  
- **RESTful Endpoints**:  
  - Well-structured API routes for user authentication and task operations.  
- **Dynamic UI**:  
  - A clean, responsive, and user-friendly interface to manage tasks.  
- **Screenshots Included**:  
  - Visual representation of the application for quick insights.

---

## 📸 Screenshots  

### Register Page  
![Register Page](https://github.com/kaushal892004/ToDo_MongoDB/blob/main/Images/registerpage.png) 

### Login Page  
![Login Page](https://github.com/kaushal892004/ToDo_MongoDB/blob/main/Images/loginpage.png) 

### AddTask Page  
![AddTask Page](https://github.com/kaushal892004/ToDo_MongoDB/blob/main/Images/addtask.png) 

### TaskDashboard Page  
![TaskDashboard Page](https://github.com/kaushal892004/ToDo_MongoDB/blob/main/Images/taskdashboard.png) 

### Feature Page  
![Feature Page](https://github.com/kaushal892004/ToDo_MongoDB/blob/main/Images/featurepage.png) 

### About Page  
![About Page](https://github.com/kaushal892004/ToDo_MongoDB/blob/main/Images/aboutpage.png) 
---

## 🛠️ Tech Stack  

- **Backend**: Flask  
- **Database**: MongoDB (via **PyMongo**)  
- **Authentication**: JWT and bcrypt  
- **Frontend**: HTML, CSS, JavaScript  

---

## 📁 Project Structure  

```plaintext  
|-- app/  
|   |-- templates/             # HTML files  
|   |-- static/                # CSS, JavaScript, and Images  
|   |-- routes.py              # API routes  
|   |-- models.py              # Data models and MongoDB schema  
|   |-- __init__.py            # Flask app initialization  
|-- config.py                  # Configuration file for Flask and database  
|-- requirements.txt           # Python dependencies  
|-- README.md                  # Project documentation  
```

---

## ⚙️ Installation  

1. **Clone the repository**  
   ```bash  
   git clone https://github.com/kaushal892004/ToDo_MongoDB.git
   cd flask-todo-app  
   ```  

2. **Set up a virtual environment**  
   ```bash  
   python -m venv venv  
   source venv/bin/activate  # On Windows: venv\Scripts\activate  
   ```  

3. **Install dependencies**  
   ```bash  
   pip install -r requirements.txt  
   ```  

4. **Set up MongoDB**  
   - Ensure MongoDB is installed and running on your system.  
   - Update the connection string in `config.py`.  

5. **Run the application**  
   ```bash  
   flask run  
   ```  

6. **Access the app**  
   Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000).  

---

## 🛡️ API Endpoints  

| Method | Endpoint          | Description                       | Authentication |  
|--------|-------------------|-----------------------------------|----------------|  
| POST   | `/signup`         | User registration                | ❌             |  
| POST   | `/login`          | User login                       | ❌             |  
| GET    | `/tasks`          | Retrieve all tasks               | ✅             |  
| POST   | `/tasks`          | Add a new task                   | ✅             |  
| PUT    | `/tasks/<id>`     | Update a specific task           | ✅             |  
| DELETE | `/tasks/<id>`     | Delete a specific task           | ✅             |  

---

## 📄 Requirements  

- Python 3.9+  
- MongoDB 4.0+  
- Flask 2.0+  
- PyMongo, Flask-JWT-Extended, bcrypt  

---

## 🌟 Future Enhancements  

- Add categories and priorities for tasks.  
- Implement task reminders via email.  
- Enhance UI/UX with modern frameworks like React or Vue.js.  
- Add real-time updates using WebSockets.  

---

## 🤝 Contribution  

Feel free to fork this repository, make changes, and submit a pull request. Contributions are always welcome!  

---


Let me know if you need help with further customizations!

### Made with ❤️ by [Kaushal Parmar](https://github.com/kaushal892004)
