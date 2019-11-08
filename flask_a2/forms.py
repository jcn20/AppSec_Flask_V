from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from flask_a2.models import User



class RegistrationForm(FlaskForm):
    uname = StringField('Username', validators=[DataRequired(), Length(min=5, max=20)])
    mfa = PasswordField('2fa', id="2fa", validators=[DataRequired(), Length(min=10, max=11)])
    pword = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_uname(self, uname):

        user = User.query.filter_by(uname=uname.data).first()
        if user:
            raise ValidationError('Failure: That username is already taken.')

    def validate_mfa(self, mfa):

        user = User.query.filter_by(mfa=mfa.data).first()
        if user:
            raise ValidationError('Failure: That number is already used for another account.')


class LoginForm(FlaskForm):
    uname = StringField('Username', validators=[DataRequired(), Length(min=5, max=20)])
    mfa = PasswordField('2fa', id="2fa", validators=[DataRequired(), Length(min=10, max=11)])
    pword = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

    def validate_creds(self, uname, mfa):

        user = User.query.filter_by(uname=uname.data, mfa=mfa.data).first()
        if not user:
            raise ValidationError('Failure: That username does not exist.')
        elif not mfa:
            raise ValidationError('Failure: Your 2fa is incorrect.')
        elif len(mfa.data) > 10:
            raise ValidationError('Failure: You should only input 10 - 11 numbers.')
        else:
            pass


class SubmitForm(FlaskForm):
    inputtext = StringField('Type your text here: ', id='inputtext', validators=[DataRequired()])
    submit = SubmitField('Submit')
