# NOT FOR PRODUCTION

import os
from flask import Flask, session
from flask import render_template, send_from_directory
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/projects")
def projects():
    return render_template('projects.html')

@app.route("/usefulinfo")
def usefulinfo():
    return render_template('usefulinfo.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    app.run(debug=True)
