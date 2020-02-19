from flask import request, jsonify, render_template

import app.helpers.predict_service as ps

def index():
    users = {"hello": "Flask!!!"}
    ps.say_hello('hello')
    return jsonify({'data': users})

#@user_blueprints.route('/home')
def home():
    return render_template('index.html')

