
from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

from .forms import RegisterForm
from .models import User, bcrypt, db


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:/
app.config["SECRET_KEY"] = "my_key"
bcrypt.init_app(app)
db.init_app(app)
csrf = CSRFProtect(app)

@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("OK")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if request.method == "POST" and form.validate():
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        password = form.password.data
        user = User(name=name, surname=surname, email=email, password=password)
        db.session.add(user)
        db.session.commit()
    return render_template("register.html", form=form)

