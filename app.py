from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = FLASK(__EComm__)
CORS(app) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'  # SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Import your routes
from routes import *

if __name__ == '__main__':
    app.run(debug=True)