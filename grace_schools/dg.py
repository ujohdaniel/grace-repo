# Importing the modules
from flask import Flask, flash, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Creating the app
app= Flask(__name__)

# Home page
@app.route('/')
def homepage():
    return render_template('home.html')

# Events page
@app.route('/events')
def events():
    return render_template('events.html')

# About us page
@app.route('/aboutus')
def about():
    return render_template('about.html')

# Contact us page
@app.route('/admissions')
def contact():
    return render_template('admissions.html')

# Services page
@app.route('/services')
def services():
    return render_template('services.html')

# On debug mode
if __name__ == '__main__':
    app.run(debug=True)
