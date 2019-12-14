from flask import current_app, render_template, url_for, flash, redirect, request, Blueprint
from flask_a2 import  db, bcrypt
from flask_a2.forms import RegistrationForm, LoginForm, SubmitForm
from flask_a2.models import User, Post, History
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime

flask_app = Blueprint('flask_app', __name__, template_folder='templates')


posts = [
        {
            }
        ]

@flask_app.route("/")
@flask_app.route("/home")
def home():
    return render_template('home.html', title='Home', posts=posts)


@flask_app.route("/about")
def about():
    return render_template('about.html', title='About')


@flask_app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('flask_app.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(uname=form.uname.data, mfa=form.mfa.data)
        user.set_password(form.pword.data)
        user.set_created_time(datetime.utcnow())
        db.session.add(user)
        db.session.commit()
        flash(f'Success: Account created for {form.uname.data}!', 'success')
        return redirect(url_for('flask_app.register'))
    if request.method == 'POST' and not form.validate():
        flash('FAILURE: Please review the options below and fill/correct any information as needed.', 'danger')
    return render_template('register.html', title='Register', form=form)


@flask_app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('flask_app.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(uname=form.uname.data).first()
        mfa = form.mfa.data
        if user and (mfa == user.mfa) and user.check_pword(form.pword.data):
            login_user(user, remember=form.remember.data)
            login_history = History(login_timestamp=datetime.utcnow(), uid=current_user.id)
            db.session.add(login_history)
            db.session.commit()
            next_page = request.args.get('next')
            flash(f'Success: Welcome, {form.uname.data}!', 'success')
            return redirect(url_for('flask_app.login'))
        elif not user:
            flash(f'FAILURE: The user, {form.uname.data}, does not exist or is incorrect!', 'danger')
        elif mfa != user.mfa:
            flash('FAILURE: Incorrect Two-factor authentication used.', 'danger')
        else:
            flash('FAILURE: Your credentials are incorrect. Please check your credentials.', 'danger')
    return render_template('login.html', title='Login', form=form)


@flask_app.route("/logout")
def logout():
    log_history = current_user.history.order_by(History.id.desc()).first()
    log_history.set_logout_time(datetime.utcnow())
    db.session.add(log_history)
    db.session.commit()
    logout_user()
    flash('SUCCESS: You have logged out.', 'success')
    return redirect(url_for('flask_app.home'))

@flask_app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')

@flask_app.after_request
def apply_caching(response):
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    return response


@flask_app.route("/spell_check", methods=['GET', 'POST'])
@login_required
def spell_check():
    form = SubmitForm()
    if form.validate_on_submit():
        post = Post(content=form.inputtext.data, user_id=current_user.id)
        post.set_result()
        db.session.add(post)
        db.session.commit()
        flash('Successfully submitted your post!', 'success')
        return render_template("spell_check.html", title='Submit Text', form=form, post=post)
    return render_template('spell_check.html', title='Submit Text', form=form)

@flask_app.after_request
def apply_caching(response):
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    return response
