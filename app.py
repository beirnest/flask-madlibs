from stories import Story, story

from flask import Flask, request, render_template

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

@app.route("/")
def word_form():
    story_terms = story.prompts
    return render_template("form.html", story_terms = story_terms)

@app.route("/story")
def show_story():
    answers_pairs = request.args
    answers = story.generate(answers_pairs)
    return render_template("story.html", answers = answers)