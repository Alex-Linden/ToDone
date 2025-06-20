import os
from dotenv import load_dotenv

from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import User, Task  # Make sure models are correctly imported
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager

app = Flask(__name__)

toolbar = DebugToolbarExtension(app)
load_dotenv()



# Get DB_URI from environment variable (useful for production/testing) or
# if not set, use development local db.
app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ['DATABASE_URL'].replace("postgres://", "postgresql://"))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

# Initialize the Debug Toolbar (Optional, for development only)
toolbar = DebugToolbarExtension(app)

# Initialize the database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import your models
from models import User, Task  # Make sure your models are defined in models.py

@app.route('/')
def home():
    return "Welcome to the ToDone App!"

# You can add more routes for user registration, tasks, etc. here

# Example: User registration endpoint (Just a placeholder for now)
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    # Placeholder logic for user registration (add your actual logic here)
    user = User(email=data['email'], first_name=data['first_name'], last_name=data['last_name'], password=data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered successfully!"})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
