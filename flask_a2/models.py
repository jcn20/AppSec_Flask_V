from datetime import datetime
from flask_a2 import db, login_manager
from flask_login import UserMixin
import subprocess
from definitions import ROOT_PATH


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(20), unique=True, nullable=False)
    # Change this next one to phone number for 2FA
    mfa = db.Column(db.String(11), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    pword = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.uname}', '{self.mfa}', '{self.image_file}')"


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

    def get_result(self):
        return self.result

    def get_date_posted(self):
        return self.date_posted

    def get_user(self):
        return User.query.get(self.user_id).uname



