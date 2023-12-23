from flask import Flask, render_template
from routes.auth import auth
from pathlib import Path

THIS_FOLDER = Path(__file__).parent.resolve()



app = Flask('User Authentication Python - Flask', root_path=THIS_FOLDER)

app.secret_key = 'secret key'
app.register_blueprint(auth)

print(app.root_path)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
