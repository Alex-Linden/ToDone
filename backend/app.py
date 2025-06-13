from flask import Flask, request, jsonify
from models import db, User, Task  # Make sure models are correctly imported

app = Flask(__name__)

# Configuration settings (use SQLite for simplicity here)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todone.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

@app.route('/')
def home():
    return "Welcome to the ToDone App!"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
