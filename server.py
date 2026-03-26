"""
This module provides a Flask-based web server for emotion detection.
It analyzes text input and returns scores for various emotions.
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """
    Renders the main index page of the application.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def sentiment_analyzer():
    """
    Analyzes the input text from the user and returns the emotion scores.
    If the input is invalid, returns an error message.
    """
    # Get text to analyze from request arguments
    text_to_analyze = request.args.get("textToAnalyze")

    # Call the emotion detection function from the package
    response = emotion_detector(text_to_analyze)

    # Extract the individual emotion scores and dominant emotion
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Handle blank or invalid input cases
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Return the formatted string response
    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
        f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
