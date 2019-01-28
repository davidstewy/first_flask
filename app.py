from flask import Flask
from tinydb import TinyDB
from flask import render_template
import random

app = Flask(__name__)
db = TinyDB('db.json')
recipes = db.all()


@app.route('/')
def hello_world():
    recipe = random.choice(recipes)
    return render_template('index.html', recipe=recipe)
