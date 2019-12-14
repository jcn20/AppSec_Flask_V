from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, validators
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from flask_a2.models import User



def number_validation(form, phone):
    if len(phone.data) > 14:
        raise ValidationError('FAILURE: Phone number is invalid - make sure to only use numbers. Only US numbers are currently allowed.')
    else:
        modified_phone = phone.data.strip(' ()-') # remove special characters that aren't needed.
        if len(modified_phone) == 10 or len(modified_phone) == 11:
            for i in range(len(modified_phone)):
                    if modified_phone[i].isnumeric():
                        continue
                    else:
                        raise ValidationError('FAILURE: Only numbers are allowed for this field.')
        else:
            raise ValidationError('FAILURE: US Numbers should have 10-11 digits with area/country codes.')

def user_validation(form, user):
    if len(user.data) > 20:
        raise ValidationError('FAILURE: Usernames can not be greater than 20 characters.')
    if len(user.data) < 5: 
      raise ValidationError('FAILURE: Usernames can not be less than 5 characters.')
    username = user.data
    for i in range(len(username)):
        if username[i].isalnum():
            continue
        else:
            raise ValidationError('FAILURE: Special characters are not allowed.')

class RegistrationForm(FlaskForm):
    uname = StringField('Username', id='uname',  validators=[user_validation, DataRequired()])
    mfa = StringField('mfa', id='2fa', validators=[number_validation, validators.Optional()])
    pword = PasswordField('Password', id='pword', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_uname(self, uname):

        user = User.query.filter_by(uname=uname.data).first()
        if user:
            raise ValidationError('Failure: That username is already taken.')


class LoginForm(FlaskForm):
    uname = StringField('Username', id='uname', validators=[user_validation, DataRequired()])
    mfa = PasswordField('2fa', id='2fa', validators=[number_validation, validators.Optional()])
    pword = PasswordField('Password', id='pword',  validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

    def validate_creds(self, uname, mfa):

        user = User.query.filter_by(uname=uname.data, mfa=mfa.data).first()
        if not user:
            raise ValidationError('Failure: That username does not exist.')
        elif not mfa:
            raise ValidationError('Failure: Your 2fa is incorrect.')
        elif len(mfa.data) > 11:
            raise ValidationError('Failure: You should only input 10 - 11 numbers.')
        else:
            pass


class SubmitForm(FlaskForm):
    inputtext = StringField('Type your text here: ', id='inputtext', validators=[DataRequired()])
    submit = SubmitField('Submit')

class UserLogActivity(FlaskForm):
    inputtext = StringField('Type your text here: ', id='userid', validators=[DataRequired()])
    submit = SubmitField('Submit')

class UserPostHistory(FlaskForm):
    inputtext = StringField('Type your text here: ', id='userquery', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
    def validate_uname(self, uname):

        user = User.query.filter_by(uname=uname.data).first()
        if user:
            raise ValidationError('Failure: That user does not exist.')

