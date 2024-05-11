import argparse

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='dist', static_url_path='')
# 数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://skycloud:skycloud@192.168.166.66:3306/db_wcnm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'Fj0opkMbP3TIYXYoa5XO'
db = SQLAlchemy(app)
CORS(app)

from routes import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, help='运行端口', default=5000)
    args = parser.parse_args()
    app.run(debug=True, port=args.port)