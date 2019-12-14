from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_a2 import db, login_manager, bcrypt
from flask_login import UserMixin
import subprocess
from datetime import datetime
from config import ROOT_PATH


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uname = db.Column(db.String(20), unique=True, nullable=False)
    # Change this next one to phone number for 2FA
    mfa = db.Column(db.String(11))
    pword = db.Column(db.String(60), nullable=False)
    post = db.relationship('Post', backref='author', lazy='dynamic')
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    queries = db.Column(db.Integer, default=0)
    admin_user = db.Column(db.Boolean, default=False) # Is the user an admin or not? Add additional functionality.
    history = db.relationship('History', backref='source_owner', lazy='dynamic')

    def get_uname(self):
        return self.uname

    def set_password(self, password):
        self.pword = bcrypt.generate_password_hash(password)

    def check_pword(self, password):
        return bcrypt.check_password_hash(self.pword, password)

    def get_id(self):
        return str(self.id)

    def get_mfa(self):
        return self.mfa

    def set_query_numbers(self, num_query):
        self.queries = num_query

    def query_incrementer(self):
        self.queries = self.queries + 1

    def get_queries(self):
        return self.queries

    def set_created_time(self, time):
        self.created = time

    def get_created_time(self):
        return self.created

    def get_admin_role(self):
        return self.admin_user()
    
    def __repr__(self):
        return f"User('{self.uname}')"
    
class History(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login_timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    logout_timestamp = db.Column(db.DateTime, index=True)
    uid = db.Column(db.Integer, db.ForeignKey('user.id'))

    def get_history_id(self):
        return str(self.id)

    def get_uid(self):
        return str(self.uid)

    def set_logout_time(self, logout_time):
        self.logout_timestamp = logout_time

    def get_logout_time(self):
        return self.logout_timestamp

    def set_login_time(self, login_time):
        self.login_timestamp = login_time

    def get_login_time(self):
        return self.login_timestamp

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    result = db.Column(db.Text)

    def __repr__(self):
        return '<Post {}>'.format(self.content)

    def set_result(self):
        f = open("temp.txt", 'w+')
        f.write(self.content)
        f.flush()

        output = subprocess.check_output([ROOT_PATH + "/a.out", "temp.txt", ROOT_PATH + "/wordlist.txt"])
        self.result= output.decode("utf-8")
        f.close()
    def set_date_posted(self, time):
        self.date_posted = time

    def get_result(self):
        return self.result

    def get_date_posted(self):
        return self.date_posted

    def get_user(self):
        return User.query.get(self.user_id).uname

    def set_content(self, query):
        self.content = query;
        self.set_result()

    def get_content(self):
        return self.content

    def get_id(self):
        return self.id

    def get_user_id(self):
        return self.user_id



