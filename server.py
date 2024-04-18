"""This is the backend server for World Cup Stadiums Site"""
# pylint: disable=global-statement

# import re
# from random import randrange
from flask import Flask
from flask import render_template#, redirect
# from flask import request, jsonify

app = Flask(__name__)

# ROUTES
@app.route('/')
def welcome():
    """
    Homescreen with quick button to start learning.
    TODO: Information block content

    Returns: render template
    """
    return render_template('index.html')

@app.route('/learn/<module>/<lesson>')
def learn(module, lesson):
    """
    Main route to organize learning into modules and track user progress

    Returns: render template
    """

    if module == "undertone":
        return undertone(lesson)
    if module == "value":
        return value(lesson)
    if module == "chroma":
        return chroma(lesson)

    return "Error 404: Page does not exist"

quiz_items = [
    ("", {
        "question": "",
        "media": []
    })
]

@app.route('/quiz/<question>')
def quiz(question):
    """
    Main route to organize learning into modules and track user progress

    Returns: render template
    """

    return render_template(quiz_items[question][0], data = quiz_items[question][1])

# MODULES - HELPER ROUTES ------------------------------

def undertone(lesson):
    """
    Undertone Module
    """
    return 0

def value(lesson):
    """
    Value Module
    """
    return 0

def chroma(lesson):
    """
    Chroma Module
    """
    return 0

# HIDDEN TEST ROUTES ------------------------------------

@app.route('/mod')
def module_subheader(
    title = "Undertone",
    description = "The subtle hue or color that lies beneath the surface of a primary color, influencing its overall appearance.",
    left_img = "https://cdn.vectorstock.com/i/500p/20/11/color-whell-to-white-vector-2992011.jpg",
    right_img = "https://cdn.vectorstock.com/i/500p/20/11/color-whell-to-white-vector-2992011.jpg"
):
    """
    Module section header test page

    Returns: render template
    """

    data = {
        "title": title,
        "description": description,
        "left": left_img,
        "right": right_img
    }

    return render_template('subheader.html', data=data)

@app.route('/dnd')
def drag_and_drop(
    colors,
    title = "Undertone",
    class1 = "COOL",
    class2 = "WARM"
):
    """
    Drag and Drop activity test page

    Returns: render template
    """

    if not colors or colors == []:
        colors = ["f53310ff", "bd0c42ff", "fc5f47ff", "ca3b1eff", "fa2f56ff", "d72942ff"]

    data = {
        "title": title,
        "class1": class1,
        "class2": class2,
        "colors": colors
    }

    return render_template('drag_and_drop.html', data=data)

@app.route('/reorder')
def reorder(
    colors,
    title = "Chroma",
    class1 = "MUTED",
    class2 = "SATURATED"
):
    """
    Reorder activity test page

    Returns: render template
    """

    if not colors or colors == []:
        colors = ["8f6190ff", "797979ff", "b055b1ff", "887086ff", "c44acaff", "9e5ca1ff"]

    data = {
        "title": title,
        "class1": class1,
        "class2": class2,
        "colors": colors
    }

    return render_template('reorder.html', data=data)

@app.route('/cc')
def color_columns():
    """
    Two Column information test page

    Returns: render template
    """

    data = {
        "title": "Undertone",
        "class1": "COOL",
        "class2": "WARM",
        "colors1": ["bd0c42ff", "fa2f56ff", "d72942ff"],
        "colors2": ["f53310ff", "ca3b1eff", "fc5f47ff"],
        "description1": """A cool red leans more towards purple, 
            suggesting calmness, depth, and similarity to ripe cranberries.""",
        "description2": """A warm red has hints of orange, embodying vibrancy, 
            energy, and resembling a fiery sunset."""
    }

    return render_template('color_columns.html', data=data)

if __name__ == '__main__':
    app.run(debug = True)
