"""This is the backend server for my Color Analysis App"""
# pylint: disable=global-statement

from random import random
from flask import Flask
from flask import render_template, redirect, url_for
from flask import jsonify, request

app = Flask(__name__)

# ROUTES --------------------------------------------------
@app.route('/')
def welcome():
    """
    Homescreen with quick button to start learning.
    TODO: Information block content

    Returns: render template
    """
    return render_template('index.html')

@app.route('/learn')
def learn_root():
    """
    Returns: redirect to first lesson
    """
    return redirect(url_for('learn', module='undertone', lesson='0'))

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

@app.route('/quiz')
def quiz_root():
    """
    Returns: redirect to first lesson
    """
    data = {
            "title": "Quiz",
            "next_lesson": "/quiz/0",
            "description": """Now that you're a true fashion girlie equipped with color theory,
            it's time to test your knowledge!""",
            "left_img": "/static/img/quiz_wheel.png",
            "right_img": "/static/img/quiz_wheel.png"
        }
    return module_subheader(data)

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
    shuffled = [('a' + str(i), x) for i, x in enumerate(data['colors'])]
    data['shuffled'] = sorted(shuffled, key=lambda k: random())
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

@app.route('/ld')
def ld():
    """
    TEST
    """
    return look_differences(data = {
            "title": "Chroma Study",
            "caption": """
                Look at the <b>subtle hints of color</b> in these ladies' skin tones.
                """,
            "image1": "https://i.pinimg.com/736x/71/ee/c1/71eec1e8e5bab02c09189cd695f22b67.jpg",
            "image2": "https://i.pinimg.com/736x/4e/ad/1b/4ead1b9bd443e8e5c9d0af537fc56a7b.jpg",
            "left1":"MUTED",
            "left2":"Low Chroma",
            "left_mini": "Suits pastel and moody colors",
            "right1":"SATURATED",
            "right2":"High Chroma",
            "right_mini": "Suits bright and intense colors",
            "colors1": ["ff89a5ff", "b0a7feff", "5294d0ff", "72eabcff", "6fc0ffff"],
            "colors2": ["ff89a5ff", "b0a7feff", "5294d0ff", "72eabcff", "6fc0ffff"],
        })
def look_differences(data):
    """
    This or that question test page

    Returns: render template
    """
    return render_template('look_differences.html', data=data)

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

# DATA ----------------------------------------------------

LESSON = ("undertone", 0)
SCORE = 0

lesson_items = {
    "undertone": [
        (module_subheader, {
            "title": "Undertone",
            "prev_lesson": "/",
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
            "prev_lesson": "/learn/undertone/0",
            "lesson_id": "undertone/1",
            "next_lesson": "/learn/undertone/2",
            "class1": "COOL",
            "class2": "WARM",
            "colors1": ["bd0c42ff", "335d9cff", "ffe47aff"],
            "colors2": ["d41f18ff", "06107cff", "ffc974ff"],
        }),
        (color_columns, {
            "title": "Undertone",
            "prev_lesson": "/learn/undertone/1",
            "lesson_id": "undertone/2",
            "next_lesson": "/learn/undertone/3",
            "class1": "COOL",
            "class2": "WARM",
            "colors1": ["bd0c42ff", "335d9cff", "ffe47aff"],
            "colors2": ["d41f18ff", "06107cff", "ffc974ff"],
            "description1": """
                <p>Cool undertones shift the primary colors toward teal blue.</p>
                <p>A cool red has berry tones and a cool yellow is like a lemon.</p>
                """,
            "description2": """
            <p>Warm undertones shift colors toward brick red.</p>
            <p>A warm blue is more purple and a warm yellow is like sunshine.</p>
            """
        }),
        (look_differences, {
            "prev_lesson": "/learn/undertone/2",
            "lesson_id": "undertone/3",
            "next_lesson": "/learn/undertone/4",
            "caption": """
                Look at the <b>subtle hints of color</b> in these ladies' skin tones.
                """,
            "image1": "/static/img/cool.jpg",
            "image2": "https://i.pinimg.com/736x/6b/f5/3c/6bf53c17c6e22d1f588bf1c7355bda2d.jpg",
            "left1":"COOL",
            "left2":"Undertone",
            "left_mini": "Pink and gray-ish tones",
            "right1":"WARM",
            "right2":"Undertone",
            "right_mini": "Orange and yellow-ish tones",
            "colors1": ["edc9baff", "d5a792ff", "c1856fff", "8c5d4dff", "6c4d42ff"],
            "colors2": ["c38666ff", "a7694dff", "864034ff", "632a1cff", "491b0dff"],
        }),
        (case_study, {
            "title": "Warm Tones in Conflict",
            "prev_lesson": "/learn/undertone/3",
            "lesson_id": "undertone/4",
            "next_lesson": "/learn/undertone/5",
            "caption": """
                <p>In warm colors, Rihanna's features hide, dimming her natural radiance. </p>
                <p>This merging effect distracts from her face, making her overall appearance 
                lackluster. The outcome is a diminished glow and a less impactful presence.</p>
                """,
            "image": "/static/img/rihanna_warm.jpg",
            "colors": ["dd9c84ff", "cd9278ff", "b98b31ff", "8c4313ff", "5d2005ff"],
            "slide": 0,
        }),
        (case_study, {
            "title": "Cool Tones in Harmony",
            "prev_lesson": "/learn/undertone/4",
            "lesson_id": "undertone/5",
            "next_lesson": "/learn/undertone/6",
            "caption": """
                <p>What a difference!</p>
                <p>Notice how your eyes go straight to her face here. She looks a lot more striking,
                allowing her features to shine rather than being overpowered. </p>
                """,
            "image": "/static/img/rihanna_cool.jpg",
            "fade_image": "/static/img/rihanna_warm.jpg",
            "colors": ["dd9c84ff", "cd9278ff", "807b73ff", "555454ff", "613924ff"],
            "slide": 1,
        }),
        (case_study, {
            "title": "Cool Tones in Conflict",
            "prev_lesson": "/learn/undertone/5",
            "lesson_id": "undertone/6",
            "next_lesson": "/learn/undertone/7",
            "caption": """
                <p>Cool tones starkly contrasts Beyoncé's warm undertone, making her skin seem more
                pale and going against her natural aura.</p>
                <p>While the contrast in tones is striking, the silver looks disconnected from her face.</p>
                """,
            "image": "/static/img/beyonce_cool.png",
            "colors": ["c0ada2ff", "e3a986ff", "b36d46ff", "58526aff", "4d2f23ff"],
            "slide": 0,
        }),
        (case_study, {
            "title": "Warm Tones in Harmony",
            "prev_lesson": "/learn/undertone/6",
            "lesson_id": "undertone/7",
            "next_lesson": "/learn/value/0",
            "caption": """
                <p>Look at her glow!</p>
                <p>Much more than in silver, gold brings out the warmth of Beyonce's skin and hair,
                creating a vibrant richness to her appearance. </p>
                """,
            "image": "/static/img/beyonce_warm.png",
            "fade_image": "/static/img/beyonce_cool.png",
            "colors": ["dfbc7bff", "e3a986ff", "b36d46ff", "9d6f39ff", "644b2fff"],
            "slide": 1,
        }),
    ],
    "value": [
        (module_subheader, {
            "title": "Value",
            "prev_lesson": "/",
            "lesson_id": "value/0",
            "next_lesson": "/learn/value/1",
            "description": """The lightness or darkness of a color, 
                determining its level of brightness or depth.""",
            "left_img": "/static/img/contrast_wheel.png",
            "right_img": "/static/img/contrast_wheel.png"
        }),
        (reorder, {
            "title": "Value",
            "prev_lesson": "/learn/value/0",
            "lesson_id": "value/1",
            "next_lesson": "/learn/value/2",
            "class1": "LIGHT",
            "class2": "DARK",
            "keywords1": "Associated with airiness, spaciousness, and crispness, creating an open ambiance.",
            "keywords2": "Associated with coziness, intimate atmospheres, and captivating intensity.",
            "colors": ["f3f3f3ff", "d9d9d9ff", "b7b7b7ff", "666666ff", "434343ff", "1e1e1eff"]
        }),
        (look_differences, {
            "prev_lesson": "/learn/value/1",
            "lesson_id": "value/2",
            "next_lesson": "/learn/value/3",
            "caption": """
                Look at the <b>difference in value</b> between these ladies'<br>hair color, eye color, and skin tone.
                """,
            "image1": "https://i.pinimg.com/736x/af/3e/13/af3e13eee0365c5fc7afc608cde6b2fb.jpg",
            "image2": "https://i.pinimg.com/736x/d3/59/1c/d3591cddd40b48c0be3b31b39bb49b59.jpg ",
            "left1":"LOW",
            "left2":"Contrast",
            "left_mini": "Very similar in value — all pale",
            "right1":"HIGH",
            "right2":"Contrast",
            "right_mini": "Very different — both light and dark",
            "colors1": ["d7d7d7ff", "c1c1c1ff", "a6a6a6ff", "939393ff", "808080ff"],
            "colors2": ["d7d7d7ff", "c1c1c1ff", "878787ff", "515151ff", "000000ff"],
        }),
        (case_study, {
            "title": "High Contrast in Harmony",
            "prev_lesson": "/learn/value/2",
            "lesson_id": "value/3",
            "next_lesson": "/learn/value/4",
            "caption": """
                <p>Kendall Jenner's dark hair, piercing brown eyes, and fair skin create a
                striking high-contrast, accentuating her features with a bold allure. </p>
                <p>This adds depth and intensity to her overall appearance, contributing to
                her iconic and unforgettable presence.</p>
                """,
            "image": "/static/img/kendall_high.png",
            "colors": ["dbb89dff", "bf8163ff", "aa5844ff", "b71302ff", "050604ff"],
            "slide": 0,
        }),
        (case_study, {
            "title": "High Contrast in Harmony",
            "prev_lesson": "/learn/value/3",
            "lesson_id": "value/4",
            "next_lesson": "/learn/value/5",
            "caption": """
                <p>Look at the range of values picked from the photo. </p>
                <p>Kendall's lightest and darkest values are very distant in tone, creating
                a high contrast palette. This complements her sharp, intense features.</p>
                """,
            "image": "/static/img/kendall_high_bw.png",
            "fade_image": "/static/img/kendall_high.png",
            "colors": ["c5c5c5ff", "aeaeaeff", "878787ff", "515151ff", "000000ff"],
            "slide": 1,
        }),
        (case_study, {
            "title": "Low Contrast in Harmony",
            "prev_lesson": "/learn/value/4",
            "lesson_id": "value/5",
            "next_lesson": "/learn/value/6",
            "caption": """
                <p>On the other hand, Anya Taylor-Joy thrives in a low-contrast palette.</p>
                <p>Bright tones with subtle contrast complement Anya Taylor-Joy's features flawlessly,
                especially her striking big eyes, accentuating their captivating allure with a soft,
                luminous glow.</p>
                """,
            "image": "/static/img/anya_low.jpg",
            "colors": ["e0d7d4ff", "e3d0b8ff", "edca9cff", "c3897eff", "c01832ff"],
            "slide": 0,
        }),
        (case_study, {
            "title": "Low Contrast in Harmony",
            "prev_lesson": "/learn/value/5",
            "lesson_id": "value/6",
            "next_lesson": "/learn/chroma/0",
            "caption": """
                <p>Look at how similar all these tones are.</p>
                <p>The reduced contrast between her hair and skin tone softens her overall appearance,
                perfectly complementing the openness of Anya's face.</p>
                """,
            "image": "/static/img/anya_low.png",
            "fade_image": "/static/img/anya_low.jpg",
            "colors": ["eaeaeaff", "d7d7d7ff", "c1c1c1ff", "a6a6a6ff", "939393ff"],
            "slide": 1,
        }),
    ],
    "chroma": [
        (module_subheader, {
            "title": "Chroma",
            "prev_lesson": "/",
            "lesson_id": "chroma/0",
            "next_lesson": "/learn/chroma/1",
            "description": """The intensity or purity of a color, defining its vividness
                or saturation within the spectrum of hues.""",
            "left_img": "/static/img/saturation_wheel.png",
            "right_img": "/static/img/saturation_wheel.png"
        }),
        (reorder, {
            "title": "Chroma",
            "prev_lesson": "/learn/chroma/0",
            "lesson_id": "chroma/1",
            "next_lesson": "/learn/chroma/2",
            "class1": "MUTED",
            "class2": "SATURATED",
            "keywords1": "Associated with tranquility, vintage aesthetics, and understated elegance.",
            "keywords2": "Associated with energy, excitement, dynamism, and impactful visuals.",
            "colors": ["989698ff", "937e96ff", "8f6191ff", "8e4d91ff", "8a378eff", "8b2c8eff"]
        }),
        (drag_and_drop, {
            "title": "Chroma",
            "prev_lesson": "/learn/chroma/1",
            "lesson_id": "chroma/2",
            "next_lesson": "/learn/chroma/3",
            "class1": "MUTED",
            "class2": "SATURATED",
            "colors1": ["93c47dff", "debb98ff", "937e96ff"],
            "colors2": ["5db736ff", "ffab40ff", "8a378eff"],
        }),
        (color_columns, {
            "title": "Chroma",
            "prev_lesson": "/learn/chroma/2",
            "lesson_id": "chroma/3",
            "next_lesson": "/learn/chroma/4",
            "class1": "MUTED",
            "class2": "SATURATED",
            "colors1": ["93c47dff", "debb98ff", "937e96ff"],
            "colors2": ["5db736ff", "ffab40ff", "8a378eff"],
            "description1": """Muted colors possess a subtle and understated quality,
                with subdued tones that evoke a sense of sophistication and refinement.""",
            "description2": """Saturated colors are vibrant and intense, exuding energy
                and making a bold statement with their vivid hues that demand attention.""",
            "long1": "",
            "long2": ""
        }),
        (look_differences, {
            "prev_lesson": "/learn/chroma/3",
            "lesson_id": "chroma/4",
            "next_lesson": "/learn/chroma/5",
            "caption": """
                Look at the <b>color intensity</b> of these ladies'
                <br>hair color, eye color, and skin tone.
                """,
            "image1": "/static/img/muted.jpg",
            "image2": "/static/img/saturated.jpg",
            "left1":"MUTED",
            "left2":"Low Chroma",
            "left_mini": "Suits pastel and moody colors",
            "right1":"SATURATED",
            "right2":"High Chroma",
            "right_mini": "Suits intense and bright colors",
            "colors1": ["efaf96ff", "eb9187ff", "aa7984ff", "7d7695ff", "61708bff"],
            "colors2": ["ffaf90ff", "f67a6fff", "cd5c74ff", "6f629dff", "375895ff"],
        }),
        (case_study, {
            "title": "Muted Colors in Conflict",
            "prev_lesson": "/learn/chroma/4",
            "lesson_id": "chroma/5",
            "next_lesson": "/learn/chroma/6",
            "caption": """
                <p>Issa Rae looks stunning, but these muted colors are holding her back.</p>
                <p>Her skin and eyes look a little dull, fighting against her naturally bright complexion.
                These colors clash with her vibrant personality and overshadow her natural charm.</p>
                """,
            "image": "/static/img/issa_low.png",
            "colors": ["884d5eff", "9d466eff", "749abcff", "3f6a6fff", "414765ff"],
            "slide": 0,
        }),
        (case_study, {
            "title": "Saturated Colors in Harmony",
            "prev_lesson": "/learn/chroma/5",
            "lesson_id": "chroma/6",
            "next_lesson": "/learn/chroma/7",
            "caption": """
                <p>She’s glowing!</p>
                <p>These saturated colors bring so much life back into Issa's face. Vibrant colors
                infuse her look with energy and charisma, perfectly mirroring her dynamic and vibrant
                personality.</p>
                """,
            "image": "/static/img/issa_high.png",
            "fade_image": "/static/img/issa_low.png",
            "colors": ["d884afff", "b35894ff", "2274afff", "175259ff", "012f53ff"],
            "slide": 1,
        }),
        (case_study, {
            "title": "Saturated Colors in Conflict",
            "prev_lesson": "/learn/chroma/6",
            "lesson_id": "chroma/7",
            "next_lesson": "/learn/chroma/8",
            "caption": """
                <p>Conversely, Reese Witherspoon feels overwhelmed by the intensity of the colors here.</p>
                <p>The bright shades make her face seem tired, pulling our attention away from her features.</p>
                """,
            "image": "/static/img/reese_high.png",
            "colors": ["ff89a5ff", "b0a7feff", "5295d0ff", "72eabcff", "6fc0ffff"],
            "slide": 0,
        }),
        (case_study, {
            "title": "Muted Colors in Harmony",
            "prev_lesson": "/learn/chroma/7",
            "lesson_id": "chroma/8",
            "next_lesson": "/quiz",
            "caption": """
                <p>Here she can breathe!</p>
                <p>Despite having a lower chroma, her cheeks seem rosier and more youthful.
                A more subdued background makes her smile and soft blue eyes the star of the show.</p>
                """,
            "image": "/static/img/reese_low.png",
            "fade_image": "/static/img/reese_high.png",
            "colors": ["ffbdcdff", "bdbcffff", "659bcbff", "95e8beff", "8cc1ebff"],
            "slide": 1,
        }),
    ]
}

quiz_items = [
    (this_or_that, {
            "id": 0,
            "pre": "",
            "question": "Which outfit is saturated/has high chroma?",
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
            "pre": "With a cool undertone,",
            "question": "she looks best in...",
            "option1": "",
            "option2": "",
            "image1": "/static/img/anne_warm.jpg",
            "image2": "/static/img/anne_cool.jpg",
            "answer": 2,
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
            "pre": "Which of these ladies' features have",
            "question": "the highest contrast?",
            "option1": "",
            "option2": "",
            "image1": "https://i.pinimg.com/736x/c3/8a/22/c38a22265aebc6210220fa9e27163ecc.jpg",
            "image2": "https://i.pinimg.com/736x/fb/cf/56/fbcf5662a34ba18ca07b0154987ddae2.jpg",
            "image3": "https://i.pinimg.com/564x/eb/da/1c/ebda1cc6a3625b39991e808236799e79.jpg",
            "image4": "https://i.pinimg.com/736x/69/e2/97/69e297dd5e2e312e2d3fa4a6da9a461d.jpg",
            "answer": 1,
    }),
    (four_options, {
            "id": 5,
            "pre": "Which purple outfit has the",
            "question": "the warmest undertone?",
            "image1": "https://i.pinimg.com/564x/fe/5a/86/fe5a866fa531037f6fc937f4388f20ac.jpg",
            "image2": "https://i.pinimg.com/736x/e6/f8/0b/e6f80b861b9089c45e7889ff4e8f5720.jpg",
            "image3": "https://i.pinimg.com/564x/68/ff/dc/68ffdcf08864c5a78a23fb3980b6bddb.jpg",
            "image4": "https://i.pinimg.com/564x/7e/c4/4f/7ec44f5f35550593d458db7742c6a830.jpg",
            "answer": 4,
    }),
    (four_options, {
            "id": 6,
            "pre": "Which pink outfit's colors are",
            "question": "muted and low contrast?",
            "image1": "https://i.pinimg.com/originals/33/c8/03/33c8034beecb68833bde88b26f5c3385.jpg",
            "image2": "https://i.pinimg.com/originals/01/a4/5a/01a45a4f7899c7493b9bc5c1382c0dd2.jpg",
            "image3": "https://i.pinimg.com/originals/34/77/03/34770356b8d4c6dca8afb3128073fbe5.jpg",
            "image4": "https://i.pinimg.com/736x/15/6b/ed/156bed7a6dcde391a83d202de3590684.jpg",
            "answer": 3,
    }),
    (four_options, {
            "id": 7,
            "pre": "Which earthy outfit's colors are",
            "question": "warm, medium contrast, and muted?",
            "image1": "https://i.pinimg.com/564x/3a/f8/76/3af8765f4b5e4cab1e5f9b1f21d73dd2.jpg",
            "image2": "https://i.pinimg.com/564x/5d/0d/20/5d0d20ac33d46e29f8b4fb4dae0cf899.jpg",
            "image3": "https://i.pinimg.com/564x/c9/af/53/c9af53290d4e8dd439b4308cd24e02ed.jpg",
            "image4": "https://i.pinimg.com/564x/1a/0a/d0/1a0ad086868aac965ce2c1cf89c3d6a3.jpg",
            "answer": 1,
    }),
    (four_options, {
            "id": 8,
            "pre": "Which business casual outfit's colors are",
            "question": "cool, high contrast, and saturated?",
            "image1": "https://i.pinimg.com/564x/e2/86/d5/e286d59cd3d26737a077d7d2d47b5812.jpg",
            "image2": "https://i.pinimg.com/736x/58/52/50/58525052c95052c33330076c5d68156b.jpg",
            "image3": "https://i.pinimg.com/736x/78/66/b9/7866b99415fa26b873177e1edf43a865.jpg",
            "image4": "https://i.pinimg.com/564x/65/b6/b0/65b6b0135b1aee1d4c9bbc3b6c8403f2.jpg",
            "answer": 4,
    }),
    (four_options, {
            "id": 9,
            "pre": "Which dress's warm undertone, medium contrast, and high chroma",
            "question": "suits her features best?",
            "image1": "/static/img/shein0.png",
            "image2": "/static/img/shein1.png",
            "image3": "/static/img/shein2.png",
            "image4": "/static/img/shein3.png",
            "answer": 4,
    }),
]

if __name__ == '__main__':
    app.run(debug = True)
