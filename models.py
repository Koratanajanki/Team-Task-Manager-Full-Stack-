from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


# =========================
# USER MODEL
# =========================

class User(UserMixin, db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(200),
        nullable=False
    )

    role = db.Column(
        db.String(20),
        default="Member"
    )


# =========================
# PROJECT MODEL
# =========================

class Project(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    description = db.Column(
        db.Text
    )

    start_date = db.Column(
        db.String(50)
    )

    end_date = db.Column(
        db.String(50)
    )

    priority = db.Column(
        db.String(20)
    )

    status = db.Column(
        db.String(20),
        default="Pending"
    )

    created_by = db.Column(
        db.Integer
    )


# =========================
# TASK MODEL
# =========================

class Task(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(100),
        nullable=False
    )

    description = db.Column(
        db.Text
    )

    start_date = db.Column(
        db.String(50)
    )

    deadline = db.Column(
        db.String(50)
    )

    status = db.Column(
        db.String(20),
        default="Pending"
    )

    assigned_to = db.Column(
        db.Integer,
        db.ForeignKey('user.id')
    )

    project_id = db.Column(
        db.Integer,
        db.ForeignKey('project.id')
    )