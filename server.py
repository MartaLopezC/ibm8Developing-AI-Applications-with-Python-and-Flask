"""Server of the emotion detector function"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """Function to read text sent by user and analyse it"""
    text_to_analyze = request.args.get('textToAnalyze')
    scores = emotion_detector(text_to_analyze)
    if scores['dominant_emotion'] is None:
        answer="Invalid text! Please try again!"
    else:
        answer=f"For the given statement, the system response is 'anger': {scores['anger']}, \
        'disgust': {scores['disgust']}, 'fear': {scores['fear']}, 'joy': {scores['joy']} and \
        'sadness': {scores['sadness']}. The dominant emotion is {scores['dominant_emotion']}."
    return answer

@app.route("/")
def render_index_page():
    """Function building front end"""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
