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
        "colors": ["f53310ff", "bd0c42ff", "fc5f47ff", "ca3b1eff", "fa2f56ff", "d72942ff"]
    }

    return render_template('drag_and_drop.html', data=data)

@app.route('/reorder')
def reorder():
    """_summary_

    Returns:
        _type_: _description_
    """

    data = {
        "title": "Chroma",
        "class1": "MUTED",
        "class2": "SATURATED",
        "colors": ["8f6190ff", "797979ff", "b055b1ff", "887086ff", "c44acaff", "9e5ca1ff"]
    }

    return render_template('reorder.html', data=data)

@app.route('/cc')
def color_columns():
    """_summary_

    Returns:
        _type_: _description_
    """

    data = {
        "title": "Undertone",
        "class1": "COOL",
        "class2": "WARM",
        "colors1": ["f53310ff", "ca3b1eff", "fc5f47ff"],
        "colors2": ["bd0c42ff", "fa2f56ff", "d72942ff"],
        "description1": """A cool red leans more towards purple, 
            suggesting calmness, depth, and similarity to ripe cranberries.""",
        "description2": """A warm red has hints of orange, embodying vibrancy, 
            energy, and resembling a fiery sunset."""
    }

    return render_template('color_columns.html', data=data)

if __name__ == '__main__':
    app.run(debug = True)
