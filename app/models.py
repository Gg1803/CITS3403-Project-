from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin # To get user_id and is_authenticated

class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable = False)
    username = db.Column(db.String(60), unique = True, nullable = False)
    age = db.Column(db.Integer, nullable = False)
    gender = db.Column(db.String(22), nullable = False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)    # hashed password
    # Added a relationship to the Entry model using user_id
    entries = db.relationship('Entry', backref='user', lazy=True)
    
    # Get user id for Flask-Login
    def get_id(self):
        return str(self.user_id)
    
    # Added helper methods for password hashing and checking
    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute.")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    # Debugging: String representation of the User object
    def __repr__(self):
        return f"<User(user_id={self.user_id}, username='{self.username}', email='{self.email}')>"

    # Debugging: Print all users in database
    @staticmethod
    def print_all_users():
        users = User.query.all()
        for user in users:
            print(user)

# Login manager setup
# This function is called to load a user from the user_id stored in the session
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Entry(db.Model):
    entry_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    sleep_datetime = db.Column(db.DateTime, nullable=False)
    wake_datetime = db.Column(db.DateTime, nullable=True)
    mood = db.Column(db.Integer, nullable=True)       # mood - indexed for future calculations
    # sleep duration - calculated from sleep and wake datetime (field not required here)
    # sleep quality - calculated from mood and sleep duration (field not required here)

    # Debugging: String representation of the Entry object
    def __repr__(self):
        return (f"<Entry(entry_id={self.entry_id}, user_id={self.user_id}, "
                f"sleep_datetime={self.sleep_datetime}, wake_datetime={self.wake_datetime}, mood={self.mood})>")

    # Debugging: Print all entries
    @staticmethod
    def print_all_entries():
        entries = Entry.query.all()
        for entry in entries:
            print(entry)