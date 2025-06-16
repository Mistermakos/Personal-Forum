from flask import Flask
from databaseManager import create_connection

create_connection()

app = Flask(__name__)
@app.route('/')
def hello_world():
    return '<h1>Hello World</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)