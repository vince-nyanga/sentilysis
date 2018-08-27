from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import Length, DataRequired

class SentimentForm(FlaskForm):
    text = TextAreaField('Enter text:', validators=[DataRequired(), Length(1,280, message='maximum number of characters allowed is 280')], render_kw={'placeholder': 'Enter text (up to 280 characters)'})
    submit = SubmitField('Get sentiment')