from TAAS import app
from flask import render_template, request, session, redirect, url_for
from TAAS import db
from TAAS.models import Customers, Administrator, Car, Journey, Booking, CModel
from datetime import datetime

@app.route('/', methods=["REG", "POST", "GET"])
def index():
    return render_template('logreg.html')


@app.route('/About')
def About():
    return render_template('About.html')


@app.route('/navbar')
def navbar():
    return render_template('navbar.html')


@app.route('/Contact')
def Contact():
    return render_template('Contact.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/display_page')
def display_page():
    return render_template('display_page.html')


@app.route('/customer_login', methods=["POST", "GET"])
def customer_login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        cust = Customers.query.filter_by(uname=username).first()
        if password == cust.password:
            print("Login")

    return redirect("/")


@app.route('/customer_register', methods=["POST", "GET"])
def customer_register():
    if request.method == "POST":
        name = request.form['name']
        uname = request.form['uname']
        password = request.form['pswd']
        pjrny = 0
        new_customer = Customers(
            name=name, uname=uname, password=password, pjrny=pjrny, jdate=datetime.utcnow())
        db.session.add(new_customer)
        db.session.commit()

    return redirect("/")


@app.route('/logout')
def logout():
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

@app.route('/adminstr')
def adminstr():
    return render_template('adminstr.html')
