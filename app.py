from flask import Flask, render_template, request, redirect, session

from models import db, User, Project, Task

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash


app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret123'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

with app.app_context():
    db.create_all()


# HOME
@app.route('/')
def home():
    return redirect('/login')


# SIGNUP
@app.route('/signup', methods=['GET', 'POST'])
def signup():

    # COUNT ADMINS
    admin_count = User.query.filter_by(role="Admin").count()

    if request.method == 'POST':

        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']

        # CHECK EXISTING EMAIL
        existing_user = User.query.filter_by(email=email).first()

        if existing_user:

            return "Email already exists"

        # LIMIT ADMINS TO 5
        if role == "Admin" and admin_count >= 5:

            return "Admin limit reached"

        # CREATE USER
        user = User(
            username=username,
            email=email,
            password=password,
            role=role
        )

        db.session.add(user)
        db.session.commit()

        return redirect('/login')

    return render_template(
        'signup.html',
        admin_count=admin_count
    )
# LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form['email']

        password = request.form['password']

        user = User.query.filter_by(
            email=email
        ).first()

        if user and check_password_hash(
            user.password,
            password
        ):

            session['user_id'] = user.id
            session['username'] = user.username
            session['role'] = user.role

            return redirect('/dashboard')

        else:
            return "Invalid Email or Password"

    return render_template('login.html')


# DASHBOARD
@app.route('/dashboard')
def dashboard():

    # Check login
    if 'user_id' not in session:
        return redirect('/login')

    role = session.get('role')

    user_id = session.get('user_id')

    # ADMIN DASHBOARD
    if role == "Admin":

        tasks = Task.query.all()

        projects = Project.query.all()

        members = User.query.filter_by(
            role="Member"
        ).all()

        total = len(tasks)

        completed = len([
            t for t in tasks
            if t.status == "Completed"
        ])

        pending = len([
            t for t in tasks
            if t.status == "Pending"
        ])

        in_progress = len([
            t for t in tasks
            if t.status == "In Progress"
        ])

        return render_template(
            'admin_dashboard.html',
            role=role,
            tasks=tasks,
            projects=projects,
            members=members,
            total=total,
            completed=completed,
            pending=pending,
            in_progress=in_progress
        )

    # MEMBER DASHBOARD
    else:

        tasks = Task.query.filter_by(
            assigned_to=user_id
        ).all()

        projects = Project.query.all()

        total = len(tasks)

        completed = len([
            t for t in tasks
            if t.status == "Completed"
        ])

        pending = len([
            t for t in tasks
            if t.status == "Pending"
        ])

        in_progress = len([
            t for t in tasks
            if t.status == "In Progress"
        ])

        return render_template(
            'member_dashboard.html',
            role=role,
            tasks=tasks,
            projects=projects,
            total=total,
            completed=completed,
            pending=pending,
            in_progress=in_progress
        )


# CREATE PROJECT
@app.route('/create-project', methods=['GET', 'POST'])
def create_project():

    if 'user_id' not in session:
        return redirect('/login')

    # GET ALL MEMBERS
    users = User.query.filter_by(role="Member").all()

    if request.method == 'POST':

        name = request.form['name']
        description = request.form['description']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        priority = request.form['priority']
        status = request.form['status']

        project = Project(
            name=name,
            description=description,
            start_date=start_date,
            end_date=end_date,
            priority=priority,
            status=status
        )

        db.session.add(project)
        db.session.commit()

        return redirect('/dashboard')

    return render_template(
        'create_project.html',
        users=users
    )
# CREATE TASK
@app.route('/create-task', methods=['GET', 'POST'])
def create_task():

    if 'user_id' not in session:
        return redirect('/login')

    role = session.get('role')

    # Only admin can create task
    if role != "Admin":
        return "Access Denied"

    users = User.query.all()

    projects = Project.query.all()

    if request.method == 'POST':

        title = request.form['title']

        description = request.form['description']

        deadline = request.form['deadline']

        assigned_to = request.form['assigned_to']

        project_id = request.form['project_id']

        task = Task(
            title=title,
            description=description,
            deadline=deadline,
            assigned_to=assigned_to,
            project_id=project_id,
            status="Pending"
        )

        db.session.add(task)

        db.session.commit()

        return redirect('/dashboard')

    return render_template(
        'create_task.html',
        users=users,
        projects=projects
    )


# UPDATE TASK STATUS
@app.route('/update-task/<int:id>', methods=['POST'])
def update_task(id):

    if 'user_id' not in session:
        return redirect('/login')

    task = Task.query.get(id)

    if not task:
        return "Task Not Found"

    task.status = request.form['status']

    db.session.commit()

    return redirect('/dashboard')


# LOGOUT
@app.route('/logout')
def logout():

    session.clear()

    return redirect('/login')


# RUN APP
import os

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )