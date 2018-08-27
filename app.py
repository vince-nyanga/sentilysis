from flask import Flask, request, jsonify
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

sid = SentimentIntensityAnalyzer()

app = Flask(__name__)

@app.route("/")
def main():
    return "App is running"

@app.route("/analyse", methods=["POST"])
def analyse_sentiment():
    text = request.json['text']
    data = sid.polarity_scores(text)
    return jsonify(data)


if(__name__ == "__main__"):
    app.run(debug=True)