from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class SentimentApi(object):

    def __init__(self):
        self.analyser = SentimentIntensityAnalyzer()

    def get_sentiment(self, text):
        if text is None:
            raise ValueError('text cannot be empty')

        return self.analyser.polarity_scores(text)

    @staticmethod
    def init_app(app):
        pass
