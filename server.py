from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def text_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    data = emotion_detector(text_to_analyze)
    response = (
        f"For the given statement, the system response is "
        f"'anger': {data['anger']}, "
        f"'disgust': {data['disgust']}, "
        f"'fear': {data['fear']}, "
        f"'joy': {data['joy']} and "
        f"'sadness': {data['sadness']}. "
        f"The dominant emotion is {data['dominant_emotion']}."
    )
    return response

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)