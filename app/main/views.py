from flask import render_template
from .import main
from ..request import get_news
# from .forms import ReviewForm
from ..models import Review


@main.route('/')
def index():
    popular_news = get_news()
    return render_template('index.html',articles = popular_news)


