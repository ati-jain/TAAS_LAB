from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customer.db'
app.config['SQLALCHEMY_BINDS'] = {'statistics': 'sqlite:///statistics.db', 'cmodel': 'sqlite:///cmodel.db',
                                  'car': 'sqlite:///car.db', 'admin': 'sqlite:///admin.db', 'booking': 'sqlite:///booking.db', 'journey': 'sqlite:///journey.db'}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Statistics(db.Model):
    __bind_key__ = 'statistics'
    id = db.Column(db.Integer, primary_key=True)
    demand = db.Column(db.Integer)
    rvnu = db.Column(db.Integer)
    prft = db.Column(db.Boolean)
    feedback = db.Column(db.Float)
    fuel = db.Column(db.Integer)
    mntnc = db.Column(db.Integer)


class CModel(db.Model):
    __bind_key__ = 'cmodel'
    __abstract__ = True
    mno = db.Column(db.Integer, primary_key=True)
    accar = db.Column(db.Integer)
    naccar = db.Column(db.Integer)
    sts = db.Column(db.Integer)


class Car(CModel):
    __bind_key__ = 'car'
    id = db.Column(db.Integer, primary_key=True)
    carno = db.Column(db.String(30), nullable=False)
    pdate = db.Column(db.DateTime, default=datetime.utcnow)
    kms = db.Column(db.Integer)
    ac = db.Column(db.Boolean)
    avl = db.Column(db.Boolean)
    fuel = db.Column(db.Integer)

    def repr(self) -> str:
        return f"{self.carno} - {self.model}"


class Administrator(db.Model):
    __bind_key__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)


class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    uname = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    jdate = db.Column(db.DateTime, default=datetime.utcnow)
    pjrny = db.Column(db.Integer)

    def repr(self) -> str:
        return f"{self.name} - {self.password} - {self.date}"


class Booking(db.Model):
    __bind_key__ = 'booking'
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    cust = db.Column(db.Integer)
    car = db.Column(db.Integer)
    bdate = db.Column(db.DateTime, default=datetime.utcnow)
    ereturn = db.Column(db.Integer)


class Journey(Booking):
    __bind_key__ = 'journey'
    id = db.Column(db.Integer, primary_key=True)
    rdate = db.Column(db.DateTime, default=datetime.utcnow)
    refund = db.Column(db.Integer)


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


if __name__ == '__main__':
    app.run(debug=True)
