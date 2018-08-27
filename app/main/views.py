from flask import redirect, render_template, url_for,flash
from app.main import bp
from .forms import SentimentForm
from app import sentiment_api as api

def process_result(result):
    sentiment = result['compound']
    if sentiment < -0.5:
        mood = 'Very sad'
    elif sentiment < 0:
        mood = 'Sad'
    elif sentiment == 0:
        mood = 'Neutral'
    elif sentiment < 0.5:
        mood = 'Happy'
    else:
        mood = 'Very happy'
    return mood

@bp.route('/', methods=['GET', 'POST'])
def index():
    form = SentimentForm()
    if form.validate_on_submit():
        text = form.text.data
        result = api.get_sentiment(text)
        flash('Sentiment: {}'.format(process_result(result)), category='teal')
        return redirect(url_for('main.index'))
    return render_template('index.html', form=form)