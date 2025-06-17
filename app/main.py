from flask import Flask
from databaseManager import init_db
from router import main_bp

app = Flask(__name__)
#connecting db
init_db()

#connecting main route
app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
