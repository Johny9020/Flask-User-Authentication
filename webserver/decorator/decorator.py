# Import wraps from functools
from functools import wraps
from flask import session, redirect, url_for


# Create the @check_logged_in decorator
def check_logged_in(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Check if the user is logged in
        if session.get('logged_in') is not None:
            # If so, call the decorated function
            return func(*args, **kwargs)

        # If not, redirect to the login page
        print('You are not logged in')
        return redirect(url_for('auth.login'))
    return wrapper
