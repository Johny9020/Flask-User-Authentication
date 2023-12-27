from flask import Flask, render_template, make_response, jsonify, request
from routes.auth import auth
from uuid import uuid4

app = Flask(__name__)
app.config['SECRET_KEY'] = '06ebbdd1857a414899e846820d512979'

app.register_blueprint(auth)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/v1')
def api():
    try:
        response = make_response(jsonify({'message': 'Hello World!'}), 200)
        response.set_cookie('session', str(uuid4()), httponly=True, samesite='Lax', secure=True)
        return response
    except:
        return jsonify({'error': 'Invalid request'}), 400


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)