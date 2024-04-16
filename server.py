"""This is the backend server for World Cup Stadiums Site"""
# pylint: disable=global-statement

# import re
# from random import randrange
from flask import Flask
from flask import render_template#, redirect
# from flask import request, jsonify

app = Flask(__name__)

regions = ["Western Region", "Central Region", "Eastern Region"]
stadiums = []

# current_id = 10

# ROUTES
@app.route('/')
def welcome():
    """_summary_

    Returns:
        _type_: _description_
    """
    return render_template('index.html')

@app.route('/dnd')
def drag_and_drop():
    """_summary_

    Returns:
        _type_: _description_
    """

    data = {
        "title": "Undertone",
        "class1": "COOL",
        "class2": "WARM",
        "colors": ["f52c10ff", "bd0c42ff", "fc5f47ff", "ca3b1eff", "fa2f56ff", "d72942ff"]
    }

    return render_template('drag_and_drop.html', data=data)

if __name__ == '__main__':
    app.run(debug = True)
