from flask import Flask , render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DecimalField,BooleanField, RadioField, SelectField,TextAreaField,FileField
from wtforms.validators import InputRequired
from werkzeug.security import generate_password_hash

app = Flask(__name__)


class MyForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    remember_me = BooleanField('Remember Me')
    gender = RadioField('Gender', choices=[('male','Male'),('female','Female')])
    salary = DecimalField('Salary', validators=[InputRequired()])
    country = SelectField('Country', choices=[('Ind','India'),('UK','United Kingdom')])
    message = TextAreaField('Message', validators=[InputRequired()])
    photo = FileField('Photo')

@app.route('/',methods=['GET','POST'])
def Home():
    form = MyForm()
    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data
        salary = form.salary.data
        gender = form.gender.data
        message = form.message.data
        remember_me = form.remember_me.data
        country = form.country.data
        photo = form.photo.data
        return f"<h1>Name:{name} <br> Password: {generate_password_hash(password)} <br> remember_me:{remember_me} <br> Salary:{salary} <br> Gender:{gender} <br> Country: {country} <br> Mesage: {message} <br> Photo:{photo}</h1>"
        #f"<h1>Name:{name} <br> assword: {generate_password_hash(password)} <br> remember_me:{remember_me} <br> Salary:{salary}</h1> 
    return render_template('index.html', form = form)

