# THIS IS THE MAIN ENTRY POINT, THIS PYTHON FILE RUNS THE APP
# CREATES FLASK APP
# LOADS CONFIGURATIONS
# IMPORTS AND REGISTERS ROUTES from routes.py
# RUNS THE FLASK SERVER
from flask import Flask, render_template

app = Flask(__name__)

# BEFORE LOGIN ROUTES
# BEFORE LOGIN ROUTES
# BEFORE LOGIN ROUTES

@app.route('/')
def landing():
    return render_template('loggedout/landing.html')

@app.route('/contactUs')
def contactUs():
    return render_template('loggedout/contactUs.html')

@app.route('/home')
def home():
    return render_template('loggedin/home.html')




























if __name__ == '__main__':
    app.run(debug=True)