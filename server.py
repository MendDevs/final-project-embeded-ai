from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emo_detector():
    """
    Analyzes the emotion of the text received as a query parameter and returns the emotion analysis.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    if text_to_analyze is None or text_to_analyze.strip() == "":
        return "Invalid text! Please provide text to analyze.", 400

    response = emotion_detector(text_to_analyze)
    if response is None:
        return "Error analyzing emotion. Please try again later.", 500

    # Check if the response contains the expected keys
    expected_keys = ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']
    if not all(key in response for key in expected_keys):
        return "Unexpected response from emotion detection service.", 500

    # Extract emotion values from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    return (
        f"For the given statement, the emotion analysis is as follows:\n"
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, 'sadness': {sadness}. \n"
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the index.html page.
    """
    return render_template('index.html')

#running the app
if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=5000)
    app.run(debug=True)
