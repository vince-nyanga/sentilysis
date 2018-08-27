from app.api import rest_api
from flask import request, jsonify
from app import sentiment_api

@rest_api.route('/analyse', methods=['POST'])
def analyze_sentiment():
    text = request.json['text']
    try:
        result = sentiment_api.get_sentiment(text)
        return jsonify(result)
    except Exception as e:
        return jsonify({
            'error': str(e)
        })