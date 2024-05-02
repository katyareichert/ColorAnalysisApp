"""This is the backend server for World Cup Stadiums Site"""
# pylint: disable=global-statement

# import re
# from random import randrange
from flask import Flask
from flask import render_template#, redirect
from flask import jsonify, request

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

    if question == 0:
        global SCORE
        SCORE = 0

    try:
        render_page, data = quiz_items[int(question)]
        return render_page(data)
    except ValueError:
        return "Error 404: Page does not exist"

@app.route('/quiz/score')
def quiz_score():
    """
    Show final quiz results
    """

    total = len(quiz_items)
    score = str(SCORE) + "/" + str(total)
    description = ""

    if SCORE > (2*total)//3:
        title = "Yaaas, queen!"
        description = """You're slaying it with an amazing score,
        showing off your fierce knowledge and style!"""

    elif SCORE > total//3:
        title = "Looking good, hun!"
        description = """Your score is on point,showing
        you've got the basics down, but there's always room to accessorize and level up."""

    else:
        title = "Go piss, girl..."
        description = """Let's glam up that score by giving
        those learn tabs another twirl, it's all about the journey, right?"""

    data = {
            "title": title,
            "description": description,
            "score": score,
            "left_img": 
                "https://cdn.vectorstock.com/i/500p/20/11/color-whell-to-white-vector-2992011.jpg",
            "right_img": 
                "https://cdn.vectorstock.com/i/500p/20/11/color-whell-to-white-vector-2992011.jpg",
        }

    return render_template('quiz_score.html', data=data)

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
        })
def this_or_that(data):
    """
    This or that question test page

    Returns: render template
    """
    return render_template('thisorthat.html', data=data)

@app.route('/cs')
def cs():
    """
    TEST
    """
    return case_study(data = {
            "title": "Chroma Study",
            "caption": """
                <p>Conversely, Reese Witherspoon feels overwhelmed by the intensity of the colors here. </p>
                <p>The bright shades make her face seem tired, pulling our attention away from her features.</p>
                """,
            "image": "/static/img/kendall_high.png",
            "colors": ["ff89a5ff", "b0a7feff", "5294d0ff", "72eabcff", "6fc0ffff"],
            "slide": 0,
        })
def case_study(data):
    """
    This or that question test page

    Returns: render template
    """
    return render_template('case_study.html', data=data)

def four_options(data):
    """
    This or that question test page

    Returns: render template
    """
    return render_template('four_options.html', data=data)

@app.route('/get_score', methods=['GET'])
def get_score():
    """
    Return the current quiz score
    """
    total = len(quiz_items)
    print(SCORE, total)
    return jsonify(score=SCORE, total=total)

@app.route('/update_score', methods=['POST'])
def update_score():
    """
    Update the quiz score
    """

    data = request.get_json()
    question_id = data["question_id"]
    correct = data["correct"]

    if correct:
        global SCORE
        SCORE += 1

    next_question_id = question_id + 1
    next_question_url = "/quiz/" + str(next_question_id)

    if next_question_id >= len(quiz_items):
        return jsonify(score=SCORE, next_question_url="/quiz/score")

    return jsonify(score=SCORE, next_question_url = next_question_url)

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
    (this_or_that, {
            "id": 0,
            "pre": "",
            "question": "Which outfit has high chroma?",
            "option1": "",
            "option2": "",
            "image1": "https://i.pinimg.com/564x/77/86/64/778664aa9712debc60f21f4e860a27ef.jpg",
            "image2": "https://www.annalauren.ca/cdn/shop/files/S605c19a39a1a4d6ab0880c2f3add2b84Z.webp?v=1706915934&width=1206",
            "answer": 2,
    }),
    (this_or_that, {
            "id": 1,
            "pre": "",
            "question": "Which outfit highlights cool tones?",
            "option1": "",
            "option2": "",
            "image1": "https://i.pinimg.com/originals/cf/ae/3e/cfae3e6037f8803296d98d7c1dd7aee6.jpg",
            "image2": "https://i.pinimg.com/originals/ed/66/25/ed6625921c8f3c4938a1006e2bf3be87.jpg",
            "answer": 1,
    }),
    (this_or_that, {
            "id": 2,
            "pre": "",
            "question": "Whos features can handle more contrast?",
            "option1": "",
            "option2": "",
            "image1": "https://i.pinimg.com/originals/a2/3f/a1/a23fa1bcb86837a3de07c4a6bad7ad06.jpg",
            "image2": "https://i.pinimg.com/564x/d0/9f/2b/d09f2bafd306de9d50eef5491ca1ad8a.jpg",
            "answer": 1,
    }),
    (this_or_that, {
            "id": 3,
            "pre": "Which dress colors look most",
            "question": "harmonious with her warm skin tone?",
            "option1": "",
            "option2": "",
            "image1": "https://i.pinimg.com/736x/45/88/9f/45889f34807714b53baae0eda6f01681.jpg",
            "image2": "https://kiskastudios.com/cdn/shop/files/032-B1.jpg?v=1704928843&width=1344",
            "answer": 2,
    }),
    (four_options, {
            "id": 4,
            "pre": "Which outfit has the",
            "question": "highest contrast between colors?",
            "image1": "https://img-va.myshopline.com/image/store/1694484096840/MichelleBluePrintedMaxiDress-2_1512x.jpg?w=1500&h=2250",
            "image2": "https://img.staticdj.com/573d245dc748b236b7f37fba9d65a46b.jpeg",
            "image3": "https://i.pinimg.com/736x/7a/54/12/7a5412dd35bf436f0ecc096d0e4c7ae7.jpg",
            "image4": "https://i.pinimg.com/736x/d6/05/6c/d6056c3c14b8e4fa9bf0d3f70f8ee9fa.jpg",
            "answer": 2,
    }),
    (four_options, {
            "id": 5,
            "pre": "Which outfit has the",
            "question": "the warmest undertone?",
            "image1": "https://i.pinimg.com/564x/b1/8e/1c/b18e1c09290d54be91130ee23538cb65.jpg",
            "image2": "https://i.pinimg.com/736x/ca/d0/9a/cad09aab91c6ca45393c61750d8d1433.jpg",
            "image3": "https://i.pinimg.com/564x/58/60/d2/5860d24df0161560c70b55ecb0ecde4f.jpg",
            "image4": "https://i.pinimg.com/564x/61/7d/2a/617d2a349b5c025a3db3ae5cf851be71.jpg",
            "answer": 4,
    }),
    (four_options, {
            "id": 6,
            "pre": "Which outfit's colors are",
            "question": "muted and low contrast?",
            "image1": "https://i.pinimg.com/originals/33/c8/03/33c8034beecb68833bde88b26f5c3385.jpg",
            "image2": "https://i.pinimg.com/originals/01/a4/5a/01a45a4f7899c7493b9bc5c1382c0dd2.jpg",
            "image3": "https://i.pinimg.com/originals/34/77/03/34770356b8d4c6dca8afb3128073fbe5.jpg",
            "image4": "https://i.pinimg.com/736x/15/6b/ed/156bed7a6dcde391a83d202de3590684.jpg",
            "answer": 3,
    }),
    (four_options, {
            "id": 7,
            "pre": "Which color blocking features a",
            "question": "50/50 mix of warm and cool?",
            "image1": "https://i.pinimg.com/736x/f4/2a/dc/f42adc7814d7aa25d6fd3d3eb8836e30.jpg",
            "image2": "https://i.pinimg.com/736x/e2/e9/ea/e2e9ea3794e35e0d036876dd6d1b99c8.jpg",
            "image3": "https://i.pinimg.com/736x/61/b7/26/61b726e03edd6f00f41a6eaa896035c5.jpg",
            "image4": "https://i.pinimg.com/736x/93/4f/a6/934fa610a3911ee217165652121fd03c.jpg",
            "answer": 3,
    }),
    (four_options, {
            "id": 8,
            "pre": "Which outfit's undertone, contrast, and chroma",
            "question": "suits her features best?",
            "image1": "/static/img/shein0.png",
            "image2": "/static/img/shein1.png",
            "image3": "/static/img/shein2.png",
            "image4": "/static/img/shein3.png",
            "answer": 4,
    }),
    (four_options, {
            "id": 9,
            "pre": "Which outfit lets you see her",
            "question": "face before the dress?",
            "image1": "/static/img/dress0.png",
            "image2": "/static/img/dress1.png",
            "image3": "/static/img/dress2.png",
            "image4": "/static/img/dress3.png",
            "answer": 2,
    }),
]

if __name__ == '__main__':
    app.run(debug = True)
