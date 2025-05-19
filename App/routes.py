from flask import Blueprint, render_template
from .models import Movie

main = Blueprint('main', __name__)

@main.route('/')
def index():
    movies = Movie.query.limit(10).all()
    return render_template('index.html', movies=movies)
