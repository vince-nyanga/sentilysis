from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import Length, DataRequired

class SentimentForm(FlaskForm):
    text = TextAreaField('Enter text:', validators=[DataRequired(), Length(1,140, message='maximum number of characters allowed is 140')], render_kw={'placeholder': 'Enter text (up to 140 characters)'})
    submit = SubmitField('Get sentiment')