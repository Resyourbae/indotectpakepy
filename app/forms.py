from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, ValidationError, Regexp
import re

def password_check(form, field):
    password = field.data
    if len(password) < 8:
        raise ValidationError('Password harus minimal 8 karakter.')
    
    if not re.search(r'[A-Z]', password):
        raise ValidationError('Password harus mengandung minimal 1 huruf kapital.')
    
    if not re.search(r'[a-z]', password):
        raise ValidationError('Password harus mengandung minimal 1 huruf kecil.')
    
    if not re.search(r'\d', password):
        raise ValidationError('Password harus mengandung minimal 1 angka.')
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        raise ValidationError('Password harus mengandung minimal 1 karakter spesial (!@#$%^&*(),.?":{}|<>).')

def email_check(form, field):
    email = field.data
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        raise ValidationError('Format email tidak valid.')
    
    domain = email.split('@')[1]
    if domain.count('.') == 0:
        raise ValidationError('Domain email tidak valid.')
    
    if len(domain.split('.')[0]) < 2:
        raise ValidationError('Domain email terlalu pendek.')
    
    if not re.match(r'^[a-zA-Z0-9].*[a-zA-Z0-9]$', email):
        raise ValidationError('Email harus dimulai dan diakhiri dengan huruf atau angka.')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(message='Username tidak boleh kosong.'),
        Length(min=3, max=150, message='Username minimal 3 karakter.')
    ])
    email = StringField('Email', validators=[
        DataRequired(message='Email tidak boleh kosong.'),
        Email(message='Format email tidak valid.'),
        email_check
    ])
    password = PasswordField('Password', validators=[
        DataRequired(message='Password tidak boleh kosong.'),
        password_check
    ])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(message='Email tidak boleh kosong.'),
        Email(message='Format email tidak valid.'),
        email_check
    ])
    password = PasswordField('Password', validators=[
        DataRequired(message='Password tidak boleh kosong.')
    ])
    submit = SubmitField('Login')

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=150)])
    bio = TextAreaField('Bio', validators=[Length(max=500)])
    phone = StringField('Phone Number', validators=[Length(max=20)])
    address = TextAreaField('Address', validators=[Length(max=200)])
    submit = SubmitField('Save Changes')
