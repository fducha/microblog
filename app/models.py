from app import db
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, DateTime
from datetime import datetime


class User(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(64), index=True, unique=True)
    email = Column(String(120), index=True, unique=True)
    password_hash = Column(String(128))
    posts = db.relationship('Post', backref='author', lazy='dinamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Post(db.Model):
    id = Column(Integer, primary_key=True)
    body = Column(String(140))
    timestamp = Column(DateTime, index=True, default=datetime.utcnow)
    user_id = Column(Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post: {}>'.format(self.body)