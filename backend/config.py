from flask import Flask;
from flask_sqlalchemy import SQLAlchemy;
from flask_cors import CORS;

# initailizing flask application
app = Flask(__name__)   
# disables the errors for CORS
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


