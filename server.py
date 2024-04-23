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
    if module not in lesson_items:
        return "Error 404: Page does not exist"

    try:
        render_page, data = lesson_items[module][int(lesson)]
        return render_page(data)
    except ValueError:
        return "Error 404: Page does not exist"

@app.route('/quiz/<question>')
def quiz(question):
    """
    Main route to organize learning into modules and track user progress

    Returns: render template
    """

    return render_template(quiz_items[question][0], data = quiz_items[question][1])

# HIDDEN HELPER ROUTES ------------------------------------

@app.route('/mod')
def mod():
    """
    TEST
    """
    return module_subheader(data = {
            "title": "Undertone",
            "description": """The subtle hue or color that lies beneath the surface
                of a primary color, influencing its overall appearance.""",
            "left_img": 
                "https://cdn.vectorstock.com/i/500p/20/11/color-whell-to-white-vector-2992011.jpg",
            "right_img": 
                "https://cdn.vectorstock.com/i/500p/20/11/color-whell-to-white-vector-2992011.jpg",
        })
def module_subheader(data):
    """
    Module section header test page

    Returns: render template
    """
    return render_template('subheader.html', data=data)

@app.route('/dnd')
def dnd():
    """
    TEST
    """
    return drag_and_drop(data = {
            "title": "Undertone",
            "class1": "COOL",
            "class2": "WARM",
            "colors1": ["bd0c42ff", "fa2f56ff", "d72942ff"],
            "colors2": ["f53310ff", "ca3b1eff", "fc5f47ff"],
        })
def drag_and_drop(data):
    """
    Drag and Drop activity test page

    Returns: render template
    """
    return render_template('drag_and_drop.html', data=data)

@app.route('/reorder')
def reor():
    """
    TEST
    """
    return reorder(data = {
            "title": "Chroma",
            "class1": "MUTED",
            "class2": "SATURATED",
            "colors": ["8f6190ff", "797979ff", "b055b1ff", "887086ff", "c44acaff", "9e5ca1ff"]
        })
def reorder(data):
    """
    Reorder activity test page

    Returns: render template
    """
    return render_template('reorder.html', data=data)

@app.route('/cc')
def cc():
    """
    TEST
    """
    return color_columns(data = {
            "title": "Undertone",
            "class1": "COOL",
            "class2": "WARM",
            "colors1": ["bd0c42ff", "fa2f56ff", "d72942ff"],
            "colors2": ["f53310ff", "ca3b1eff", "fc5f47ff"],
            "description1": """A cool red leans more towards purple, 
                suggesting calmness, depth, and similarity to ripe cranberries.""",
            "description2": """A warm red has hints of orange, embodying vibrancy, 
                energy, and resembling a fiery sunset."""
        })
def color_columns(data):
    """
    Two Column information test page

    Returns: render template
    """
    return render_template('color_columns.html', data=data)

@app.route('/tot')
def tot():
    """
    TEST
    """
    return this_or_that(data = {
            "question": "Which outfit has high chroma?",
            "option1": "",
            "option2": "",
            "image1": "https://i.pinimg.com/564x/77/86/64/778664aa9712debc60f21f4e860a27ef.jpg",
            "image2": "https://www.annalauren.ca/cdn/shop/files/S605c19a39a1a4d6ab0880c2f3add2b84Z.webp?v=1706915934&width=1206",
            "answer": 2,
            "score": 2,
        })
def this_or_that(data):
    """
    This or that question test page

    Returns: render template
    """
    return render_template('thisorthat.html', data=data)

# DATA

LESSON = ("undertone", 0)
SCORE = 0

lesson_items = {
    "undertone": [
        (module_subheader, {
            "title": "Undertone",
            "lesson_id": "undertone/0",
            "next_lesson": "/learn/undertone/1",
            "description": """The subtle hue or color that lies beneath the
                surface of a primary color, influencing its overall appearance.""",
            "left_img": 
                "https://cdn.vectorstock.com/i/500p/20/11/color-whell-to-white-vector-2992011.jpg",
            "right_img": 
                "https://cdn.vectorstock.com/i/500p/20/11/color-whell-to-white-vector-2992011.jpg"
        }),
        (drag_and_drop, {
            "title": "Undertone",
            "lesson_id": "undertone/1",
            "next_lesson": "/learn/undertone/2",
            "class1": "COOL",
            "class2": "WARM",
            "colors1": ["bd0c42ff", "fa2f56ff", "d72942ff"],
            "colors2": ["f53310ff", "ca3b1eff", "fc5f47ff"],
        }),
        (color_columns, {
            "title": "Undertone",
            "lesson_id": "undertone/2",
            "next_lesson": "/learn/undertone/1",
            "class1": "COOL",
            "class2": "WARM",
            "colors1": ["bd0c42ff", "fa2f56ff", "d72942ff"],
            "colors2": ["f53310ff", "ca3b1eff", "fc5f47ff"],
            "description1": """A cool red leans more towards purple, 
                suggesting calmness, depth, and similarity to ripe cranberries.""",
            "description2": """A warm red has hints of orange, embodying vibrancy, 
                energy, and resembling a fiery sunset.""",
            "long1": """Cool colors evoke a peaceful atmosphere, inviting exploration
                with a newfound sense of clarity and wonder.""",
            "long2": """Warm colors awaken a feeling of energy and vibrancy, igniting
                a newfound appreciation for the richness of the world."""
        })
    ],
    "value": [
        (module_subheader, {
            "title": "Value",
            "description": """The subtle hue or color that lies beneath the
                surface of a primary color, influencing its overall appearance.""",
            "left_img": 
                "https://cdn.vectorstock.com/i/500p/20/11/color-whell-to-white-vector-2992011.jpg",
            "right_img": 
                "https://cdn.vectorstock.com/i/500p/20/11/color-whell-to-white-vector-2992011.jpg"
        }),
        (color_columns, {
            "title": "Value",
            "class1": "COOL",
            "class2": "WARM",
            "colors1": ["bd0c42ff", "fa2f56ff", "d72942ff"],
            "colors2": ["f53310ff", "ca3b1eff", "fc5f47ff"],
            "description1": """A cool red leans more towards purple, 
                suggesting calmness, depth, and similarity to ripe cranberries.""",
            "description2": """A warm red has hints of orange, embodying vibrancy, 
                energy, and resembling a fiery sunset.""",
            "long1": """Cool colors evoke a peaceful atmosphere, inviting exploration
                with a newfound sense of clarity and wonder.""",
            "long2": """Warm colors awaken a feeling of energy and vibrancy, igniting
                a newfound appreciation for the richness of the world."""
        })
    ]
}

quiz_items = [
    ("thisorthat.html", {
        "question": "",
        "media": []
    })
]

if __name__ == '__main__':
    app.run(debug = True)
