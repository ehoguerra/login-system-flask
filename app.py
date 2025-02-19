import os
from flask import Flask, render_template, request
from system import register, login
 


app = Flask(__name__) 
id = 1
@app.route('/', methods=["GET", "POST"])
def register_page():
    name = request.form.get("name")
    email = request.form.get("email")
    pw1 = request.form.get("pass")
    pw2 = request.form.get("re_pass")
    #print(name, email, pw1, pw2)
    register(name, email, pw1, pw2)
    return render_template('register.html')


@app.route('/login', methods=["GET", "POST"])
def login_page():
    email = request.form.get("email")
    password = request.form.get("password")
    login(email, password)
    return render_template('login.html')
