# server/app.py

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import logging

# Import configurations
from config import Config

# Create a Flask application instance
app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database
db = SQLAlchemy(app)

# Create a Migrate object to manage schema modifications
migrate = Migrate(app, db)

# Initialize the Flask application to use the database
db.init_app(app)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Register Blueprints here (if any)
# from yourmodule import your_blueprint
# app.register_blueprint(your_blueprint)

# Define a simple route for testing
@app.route('/')
def home():
    return "Welcome to the Flask app!"

# Error handling
@app.errorhandler(404)
def not_found_error(error):
    return "This resource was not found", 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return "Internal server error", 500

if __name__ == '__main__':
    app.run(port=5555)
