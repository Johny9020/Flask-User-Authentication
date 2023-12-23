from flask import Blueprint, render_template, request, redirect, session, url_for
from webserver.database.database import insert_user, check_password, get_user
import jwt

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        found_user = get_user(username)

        if found_user and check_password(password, found_user['password']):
            # JWT Code
            print("Logged in successfully")
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error='Invalid user')

    return render_template('login.html')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_exists = get_user(request.form['username'])

        if user_exists:
            return render_template('register.html', error='Username already taken')

        username = request.form['username']
        password = request.form['password']

        insert_user(username, password)

        first_name = request.form['first_name']
        last_name = request.form['last_name']
        address = request.form['address']
        dob = request.form['dob']
        email = request.form['email']

        json = {'username': username, 'first_name': first_name, 'last_name': last_name, 'address': address, 'dob': dob,
                'email': email}

        # TODO: JWT Code
        print("Registered successfully")
        return redirect(url_for('home'))

    return render_template('register.html')
