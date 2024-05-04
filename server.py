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
    return redirect(url_for('quiz', question='0'))

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
            "colors1": ["bd0c42ff", "fa2f56ff", "d72942ff"],
            "colors2": ["f53310ff", "ca3b1eff", "fc5f47ff"],
        }),
        (color_columns, {
            "title": "Undertone",
            "prev_lesson": "/learn/undertone/1",
            "lesson_id": "undertone/2",
            "next_lesson": "/learn/undertone/3",
            "class1": "COOL",
            "class2": "WARM",
            "colors1": ["bd0c42ff", "fa2f56ff", "d72942ff"],
            "colors2": ["f53310ff", "ca3b1eff", "fc5f47ff"],
            "description1": """A cool red leans more towards purple, 
                suggesting calmness, depth, and similarity to ripe cranberries.""",
            "description2": """A warm red has hints of orange, embodying vibrancy, 
                energy, and resembling a fiery sunset."""
        }),
        (drag_and_drop, {
            "title": "Undertone",
            "prev_lesson": "/learn/undertone/2",
            "lesson_id": "undertone/3",
            "next_lesson": "/learn/undertone/4",
            "class1": "COOL",
            "class2": "WARM",
            "colors1": ["123a75ff", "335d9bff", "6081afff"],
            "colors2": ["06107cff", "2437e6ff", "6c77eaff"],
        }),
        (color_columns, {
            "title": "Undertone",
            "prev_lesson": "/learn/undertone/3",
            "lesson_id": "undertone/4",
            "next_lesson": "/learn/undertone/5",
            "class1": "COOL",
            "class2": "WARM",
            "colors1": ["123a75ff", "335d9bff", "6081afff"],
            "colors2": ["06107cff", "2437e6ff", "6c77eaff"],
            "description1": """A cool blue leans more teal or gray, evoking a sense of
                tranquility, akin to the hue of a calm ocean or a clear sky at twilight. 
                """,
            "description2": """A warm blue is more vibrant and purple, imbuing it with energy,
                reminiscent of a tropical paradise.
                """,
            "long1": "",
            "long2": ""
        }),
        (case_study, {
            "title": "Warm Tones in Conflict",
            "prev_lesson": "/learn/undertone/4",
            "lesson_id": "undertone/5",
            "next_lesson": "/learn/undertone/6",
            "caption": """
                <p>In warm colors, Rihanna's features hide, dimming her natural radiance. </p>
                <p>This merging effect distracts from her face, making her overall appearance 
                lackluster. The outcome is a diminished glow and a less impactful presence.</p>
                """,
            "image": "/static/img/rihanna_warm.jpg",
            "colors": ["cda07eff", "dd9c84ff", "b98b31ff", "8c4313ff", "5d2005ff"],
            "slide": 0,
        }),
        (case_study, {
            "title": "Cool Tones in Harmony",
            "prev_lesson": "/learn/undertone/5",
            "lesson_id": "undertone/6",
            "next_lesson": "/learn/undertone/7",
            "caption": """
                <p>What a difference!</p>
                <p>Notice how your eyes go straight to her face here. She looks a lot more striking,
                allowing her features to shine rather than being overpowered. </p>
                """,
            "image": "/static/img/rihanna_cool.jpg",
            "fade_image": "/static/img/rihanna_warm.jpg",
            "colors": ["d7b99fff", "dd9c84ff", "807b73ff", "555454ff", "613924ff"],
            "slide": 1,
        }),
        (case_study, {
            "title": "Cool Tones in Conflict",
            "prev_lesson": "/learn/undertone/6",
            "lesson_id": "undertone/7",
            "next_lesson": "/learn/undertone/8",
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
            "prev_lesson": "/learn/undertone/7",
            "lesson_id": "undertone/8",
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
        (case_study, {
            "title": "High Contrast in Harmony",
            "prev_lesson": "/learn/value/1",
            "lesson_id": "value/2",
            "next_lesson": "/learn/value/3",
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
            "prev_lesson": "/learn/value/2",
            "lesson_id": "value/3",
            "next_lesson": "/learn/value/4",
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
            "title": "Low Contrast in Conflict",
            "prev_lesson": "/learn/value/3",
            "lesson_id": "value/4",
            "next_lesson": "/learn/value/5",
            "caption": """
                <p>The reduced contrast between her hair and skin tone softened her overall appearance,
                diminishing the dramatic impact of her features. </p>
                <p>This change shifted the balance, altering the harmony of her natural aesthetic.</p>
                """,
            "image": "/static/img/kendall_low.png",
            "colors": ["dbb89dff", "bf7f63ff", "b8a786ff", "a37f4dff", "6c4436ff"],
            "slide": 0,
        }),
        (case_study, {
            "title": "Low Contrast in Conflict",
            "prev_lesson": "/learn/value/4",
            "lesson_id": "value/5",
            "next_lesson": "/learn/value/6",
            "caption": """
                <p>See how the range of values has changed from Kendall's first photo.</p>
                <p>Clearly, the range of values is smaller, all concentrated on the light end
                of the value scale. This conflicts with her features, creating a dissonant look.</p>
                """,
            "image": "/static/img/kendall_low_bw.png",
            "fade_image": "/static/img/kendall_low.png",
            "colors": ["eaeaeaff", "d7d7d7ff", "c1c1c1ff", "a6a6a6ff", "808080ff"],
            "slide": 1,
        }),
        (case_study, {
            "title": "Low Contrast in Harmony",
            "prev_lesson": "/learn/value/5",
            "lesson_id": "value/6",
            "next_lesson": "/learn/value/7",
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
            "prev_lesson": "/learn/value/6",
            "lesson_id": "value/7",
            "next_lesson": "/learn/value/8",
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
        (case_study, {
            "title": "High Contrast in Conflict",
            "prev_lesson": "/learn/value/7",
            "lesson_id": "value/8",
            "next_lesson": "/learn/value/9",
            "caption": """
                <p>High contrast doesn't flatter her features as it can overwhelm her delicate
                complexion and draw attention away from her natural elegance.</p>
                <p>She also looks less confident!</p>
                """,
            "image": "/static/img/anya_high.jpg",
            "colors": ["ecc9bfff", "deaf9eff", "b21703ff", "63191bff", "272526ff"],
            "slide": 0,
        }),
        (case_study, {
            "title": "High Contrast in Conflict",
            "prev_lesson": "/learn/value/8",
            "lesson_id": "value/9",
            "next_lesson": "/learn/chroma/0",
            "caption": """
                <p>The value range has totally changed!</p>
                <p>Here, the extremely dark hair, makeup, and clothes look completely separate
                from Anya's fair complexion. She looks almost eerie, far too intense for her
                round eyes and cheekbones.</p>
                """,
            "image": "/static/img/anya_high.png",
            "fade_image": "/static/img/anya_high.jpg",
            "colors": ["cdcdcdff", "aeaeaeff", "919191ff", "404040ff", "000000ff"],
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
        (case_study, {
            "title": "Muted Colors in Conflict",
            "prev_lesson": "/learn/chroma/3",
            "lesson_id": "chroma/4",
            "next_lesson": "/learn/chroma/5",
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
            "prev_lesson": "/learn/chroma/4",
            "lesson_id": "chroma/5",
            "next_lesson": "/learn/chroma/6",
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
            "prev_lesson": "/learn/chroma/5",
            "lesson_id": "chroma/6",
            "next_lesson": "/learn/chroma/7",
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
            "prev_lesson": "/learn/chroma/6",
            "lesson_id": "chroma/7",
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
            "image2": "https://i.pinimg.com/736x/fb/cf/56/fbcf5662a34ba18ca07b0154987ddae2.jpg",
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
            "image2": "https://i.pinimg.com/736x/69/22/32/69223223f009a553b08879a2bfc0e1a0.jpg",
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
