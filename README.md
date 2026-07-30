# 📅 DailyDocket – Engineer's Daily Planner

**DailyDocket** is a Django-based productivity and planning web application designed especially for engineering students. It helps students organize their daily activities, manage tasks, track expenses, prepare for exams, monitor projects, and improve productivity through an interactive dashboard.

---

## 🚀 Features

### 📝 Note My Day

Write and manage daily notes to keep track of important activities and plans.

### ✅ To-Do List

Create, update, complete, and delete tasks with priority management.

### 💰 Daily Expenditure Tracker

Track daily expenses and manage spending records with a dedicated expenditure management system.

### 🧠 Daily Quiz

Attempt quizzes and improve knowledge through interactive quiz functionality.

### 🔐 Email OTP Verification

Secure user registration with email-based OTP verification.

### 👤 User Authentication

Includes user signup, login, logout, and authentication features.

### 📈 Dashboard

A centralized dashboard to access different productivity and planning features.

### 🔌 REST API

Includes a REST API for managing expenditure data using Django REST Framework.

---

## 🛠️ Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap

### Backend

* Python
* Django
* Django REST Framework

### Database

* SQLite

### Tools & Technologies

* Git
* GitHub
* VS Code

---

## 📂 Project Structure

```text
DailyDocket/
│
├── Eplanner/
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── asgi.py
│   └── wsgi.py
│
├── app/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── serializers.py
│   └── urls.py
│
├── manage.py
├── db.sqlite3
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/RathodGayatri/DailyDocket-Eplanner.git
```

### 2. Navigate to the Project Directory

```bash
cd DailyDocket-Eplanner
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

For Git Bash:

```bash
source venv/Scripts/activate
```

### 5. Install Dependencies

```bash
pip install django djangorestframework
```

### 6. Run Database Migrations

```bash
python manage.py migrate
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

### 8. Open in Browser

```text
http://127.0.0.1:8000/
```

---

## 🔑 Main Application Modules

| Module              | Description                                |
| ------------------- | ------------------------------------------ |
| User Authentication | Signup, Login, Logout and OTP Verification |
| Dashboard           | Centralized access to application features |
| To-Do List          | Manage daily tasks and priorities          |
| Note My Day         | Maintain daily notes                       |
| Expenditure         | Track daily expenses                       |
| Time Tracker        | Monitor time spent on activities           |
| Exam Tracker        | Manage exam preparation                    |
| Project Tracker     | Track project progress                     |
| Daily Quiz          | Interactive quiz functionality             |
| REST API            | Expenditure management API                 |

---

## 🎯 Project Objective

The main objective of DailyDocket is to provide engineering students with a single platform where they can manage their daily tasks, academic activities, projects, expenses, and productivity.

Instead of using multiple applications for different activities, DailyDocket brings essential student productivity tools together in one web application.

---

## 🔮 Future Enhancements

* AI-powered study planning
* Advanced productivity analytics
* Push notifications and reminders
* Cloud database integration
* Mobile application
* Advanced reporting and data visualization
* Deployment on cloud platforms

---

## 👩‍💻 Developer

**Gayatri Uday Rathod**

BE Computer Engineering Graduate
Aspiring Software Engineer | Java Full Stack Developer

---

## 📌 Repository

GitHub Repository:
https://github.com/RathodGayatri/DailyDocket-Eplanner

---

⭐ If you find this project useful, consider giving it a star!
