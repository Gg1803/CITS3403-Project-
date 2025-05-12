# CITS3403-Project
CITS3403 - Agile Web Development Project

## Description: 

The Sleep Tracker is a Flask-based web application that helps users monitor and improve their sleep habits. Users can log sleep and wake times, rate how they felt upon waking, and view weekly summaries through interactive charts. The app features a calendar view for tracking daily records and a clean, mobile-friendly interface built with Tailwind CSS.


## Group Members: UWA ID, Name and Github Username
| Student ID | Student Name     | GitHub Username |
|------------|------------------|-----------------|
| 23399936   | Liam O'Brien     | limeken         |
| 23722854   | Chloe Chang      | chloetychang    |
| 23887876   | Gargi Garg       | Gg1803          |
| 24115877   | Kimberley Lee    | kimberley25     |


## Instructions: How to launch the application

### Virtual Environment
Set up the virtual environment using the following commands:

```bash
python -m venv venv
source venv/bin/activate    # In windows, use `venv\Scripts\activate`
```

### Project Dependencies
Install dependencies using the command:
```bash
pip install -r requirements.txt
```

When a dependency has been added, the requirements file should be updated with the command `pip freeze > requirements.txt`.

### Launching the Application
After setting up the virtual environment and installing the dependencies, run the command:

```bash
flask run
```

(For development, so the server does not have to be stopped and reran as we create modifications, run `flask run --debug`)

### Initialise the Database
To initialise the database, run: 
```bash
flask db upgrade
```
This will create the database and apply both existing migrations (initial and second).

## Instructions: How to run the tests for the application

There are no automated test scripts included at this stage.
You can manually test the application by:

- Registering a user

- Logging in

- Adding sleep records

- Viewing results and graphs

## Tech Stack

Backend: Python, Flask, Flask-SQLAlchemy, Flask-Login, Flask-WTF

Frontend: Tailwind CSS, Plotly.js, Jinja2 templates

Database: SQLite (via SQLAlchemy)

Utilities: Flask-Migrate, JavaScript (for flash messages and popups)

## 📁 Project Structure

CITS3403-Project/
├── app/
│   ├── __init__.py       # App config and factory
│   ├── routes.py         # Routes and logic
│   ├── models.py         # DB models (User, Entry)
│   ├── forms.py          # WTForms
│   ├── plot.py           # Graph generation
│   ├── templates/        # HTML pages
│   └── static/           # JS, icons
├── migrations/           # DB migration scripts
├── app.db                # SQLite DB (auto-generated)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation


## 🚀 Getting Started

### 🔐 Login Credentials

You can use the following test account to log in:

- **Username**: `admin`  
- **Email**: `admin@example.com`  
- **Password**: `admin123`

### 📝 Sign Up

New users can create an account by providing basic details like name, age, and email, then log in to begin tracking their sleep.


## 🧭 App Navigation

- **Sleep Page**: Upload your sleep and wake times, rate your mood, and manage entries.
- **Records Page**: View a calendar with all your logged entries; edit or add new ones.
- **Results Page**: Visualize your weekly sleep trends using an interactive Plotly graph.
- **Logout**: Securely end your session anytime using the logout option.
