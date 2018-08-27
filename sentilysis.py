from app import create_app, sentiment_api

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return dict (
        api = sentiment_api
    )