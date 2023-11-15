from flask import Flask, render_template, request, redirect, url_for
import json # We could use this to make a post request later
import requests # we'll use this to get data from forms
import random # we'll use this to generate random welcomes

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    activities = ["studying", "thinking", "learning", "revision"]
    return render_template('about.html', activity=random.choice(activities))

# run the app
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, host='0.0.0.0', port=8000)