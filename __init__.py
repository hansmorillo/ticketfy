# THIS IS THE MAIN ENTRY POINT, THIS PYTHON FILE RUNS THE APP
# CREATES FLASK APP
# LOADS CONFIGURATIONS
# IMPORTS AND REGISTERS ROUTES from routes.py
# RUNS THE FLASK SERVER
import os
import secrets
from flask import Flask, render_template

app = Flask(__name__)

# Secure Secret Key Implementation
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', secrets.token_hex(32))

# BEFORE LOGIN ROUTES
# BEFORE LOGIN ROUTES
# BEFORE LOGIN ROUTES

@app.route('/')
def landing():
    return render_template('loggedout/landing.html')

@app.route('/contactUs')
def contactUs():
    return render_template('loggedout/contactUs.html')

@app.route('/login')
def login():
    return render_template('loggedout/login.html')













# AFTER LOGIN ROUTES
# AFTER LOGIN ROUTES
# AFTER LOGIN ROUTES

@app.route('/loggedinhome')
def loginhome():
    return render_template('loggedin/loggedinhome.html')















if __name__ == '__main__':
    app.run(debug=True)


# TO DO:
# 1. Create sign-in/register
# 2. Routing
# 3. Check Header to see if need new for logged-in
