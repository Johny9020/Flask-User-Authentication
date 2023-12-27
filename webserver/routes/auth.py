from flask import Blueprint, render_template, request, redirect, url_for, make_response, jsonify
from webserver.database.database import insert_user, get_user_by_username
from webserver.models.user_model import User
from uuid import uuid4

auth = Blueprint('auth', __name__)


# TODO: Change Login function. Get UUID4() token from database and store it in the cookie
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        found_user = get_user_by_username(username)

        if found_user:
            # JWT Code
            print("Logged in successfully")
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error='Invalid user')

    return render_template('login.html')


@auth.route('/api/v1/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        address = request.form['address']
        dob = request.form['dob']
        email = request.form['email']

        try:
            # Create a new user
            new_user = User(username, password, email, first_name, last_name, address, dob, str(uuid4()))

            # Insert the user into the database
            insert_user(new_user.username, new_user.password, new_user.session_token)
            response_json = new_user.to_json()

            # Check if the request is coming from the API
            if request.headers.get('APIv1Access') == 'true':
                return response_json, 201

            # Redirect the user to the home page
            response = make_response(redirect(url_for('home')), 302)
            response.set_cookie('session', new_user.session_token, httponly=True, samesite='Lax', secure=True)
            return response
        except ValueError as e:
            return render_template('register.html', error=str(e))

    return render_template('register.html')


