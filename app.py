from flask import Flask, render_template, request
from stories import story

app = Flask(__name__)

@app.route('/')
def form():
    nums = ['verb', 'adjective', 'name', 'noun', 'proper noun', 'place']
    """Create form for user answers"""
    prompts = story.prompts
    return render_template('base.html', prompts=prompts)

@app.route('/user-story')
def user_story():
    template = story.generate(request.args)
    return render_template('user-story.html', template=template)

