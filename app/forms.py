from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange, Email
#import database form once created

class HouseInputForm(FlaskForm):
    address = StringField('Address', validators=[DataRequired(), Length(min=2, max=200)])
    price = IntegerField('Price', validators=[DataRequired(), NumberRange(min=1)])
    rent = IntegerField('Rent', validators=[DataRequired(), NumberRange(min=1)])
    rooms = IntegerField('Rooms', validators=[DataRequired(), NumberRange(min=1)])
    taxes = IntegerField('Taxes', validators=[DataRequired(), NumberRange(min=1)])
    submit = SubmitField('Submit House') 


class ResultForm(FlaskForm):
    address = StringField('Address', validators=[DataRequired(), Length(min=2, max=200)])
    price = IntegerField('Price', validators=[DataRequired(), NumberRange(min=1)])
    rent = IntegerField('Rent', validators=[DataRequired(), NumberRange(min=1)])
    rooms = IntegerField('Rooms', validators=[DataRequired(), NumberRange(min=1)])
    taxes = IntegerField('Taxes', validators=[DataRequired(), NumberRange(min=1)])


class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    confirm_password = StringField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register User')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
