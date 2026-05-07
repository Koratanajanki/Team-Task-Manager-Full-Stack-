# Team Task Manager

##  Project Overview

Team Task Manager is a full-stack web application developed using Flask and SQLite.  
This application helps organizations manage projects, assign tasks to team members, and track task progress using role-based access control.

---

#  Features

##  Authentication
- User Signup
- User Login
- Logout Functionality

---

#  Admin Features

- Create Projects
- Create Tasks
- Assign Tasks to Members
- View All Tasks
- View All Projects
- Monitor Team Status
- Dashboard Analytics

---

# Member Features

- View Assigned Projects
- View Assigned Tasks
- Update Task Status
- Monitor Progress
- View Personal Profile

---

# Dashboard Features

- Total Tasks
- Completed Tasks
- Pending Tasks
- In Progress Tasks
- Project Status Tracking
- Task Status Monitoring

---

# Technologies Used

- Python
- Flask
- Flask SQLAlchemy
- HTML5
- CSS3
- SQLite
- Jinja2 Templates

---

# Project Structure

team-task-manager/
│
├── app.py
├── models.py
├── requirements.txt
├── Procfile
├── README.md
├── .gitignore
├── database.db
│
├── static/
│ └── style.css
│
├── templates/
│ ├── loginn.html
│ ├── signup.html
│ ├── admin_dashboard.html
│ ├── member_dashboard.html
│ ├── create_project.html
│ └── create_task.html

---

#  Installation Steps

##  Clone Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

---

##  Open Project Folder

```bash
cd team-task-manager
```

---

##  Create Virtual Environment

```bash
python -m venv venv
```

---

##  Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

---

## Install Requirements

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
python app.py
```

---

#  Deployment

Application deployed using Railway.

Live URL:

Add your Railway deployment link here.

---



#  Role-Based Access

## Admin
- Full access to projects and tasks
- Can assign tasks to members

## Member
- Limited access means only 5 admins to this app
- members Can update assigned task status only

---

# Future Enhancements

- Email Notifications
- Password Encryption
- Task Search Feature
- Charts & Analytics
- Dark Mode
- Real-Time Notifications

---





# 📄 License

This project is developed for educational and internship assessment purposes.
