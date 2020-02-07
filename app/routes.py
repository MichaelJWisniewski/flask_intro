from app import app, db
from flask import render_template, redirect, flash

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/profile')
def profile():
    context = dict(
        username='derek_codingtemple',
        email='derekh@codingtemple.com' 
    )
    return render_template('profile.html', **context)

@app.route('/students')
def students():
    context = {
        'students': ["Abiola", "Michael", "Sagar", "Derek M", "Derek H"]
    }
    return render_template('students.html', **context)














