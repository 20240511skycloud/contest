from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    c_username = db.Column(db.String(64), index=True, unique=True)
    c_passwd = db.Column(db.String(128))

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    c_title = db.Column(db.String(140))
    c_description = db.Column(db.Text)
    c_user_id = db.Column(db.Integer)
    c_status = db.Column(db.Integer)