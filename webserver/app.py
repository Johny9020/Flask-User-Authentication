from flask import Flask, render_template
from routes.auth import auth

app = Flask('User Authentication Python - Flask')
app.secret_key = 'secret key'
app.register_blueprint(auth)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
