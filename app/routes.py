from flask import render_template, redirect, url_for, request
from app import app
from app.models import House
from app.forms import HouseInputForm, LoginForm, RegisterForm

house = {}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    form = LoginForm()
    user = User(
            username = form.username.data, email = form.email.data,
            password = form.password.data, confirm_password = form.confirm_password.data
            )
    return render_template('login.html', title='Log In', form=form)

@app.route('/register')
def register():
    form = RegisterForm()
    if request.method == 'POST':
        user = User(
                username = form.username.data, email = form.email.data,
                password = form.password.data, confirm_password = form.confirm_password.data
                )
        db.session.add(user)
        db.session.commit()
        return redirect( url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/house/result')
def result():
    return render_template('results.html', title='Home Result', house=house)

@app.route('/house', methods=['GET', 'POST'])
def house_input():
    form = HouseInputForm()
    if request.method == 'POST':
        #temporary print statment to show the form info is coming through
        #user = User(address=form.address.data, price=form.price.data, rent=form.rent.data, rooms=form.rooms.data, taxes=form.taxes.data, profit=0)
        house['address'] = form.address.data
        house['price'] = form.price.data
        house['rent'] = form.rent.data
        return redirect( url_for('result'))
    return render_template('house_input.html', title='Analyze a Home', form=form)
