from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    try:        
        text_to_analyze = request.args.get("textToAnalyze", "")        
        if not text_to_analyze.strip():
            return "Please provide a valid text to analyze.", 400
        
        result = emotion_detector(text_to_analyze)
        response_message = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, 'joy': {result['joy']} and "
            f"'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )

        return response_message

    except Exception as e:
        return str(e), 500

if __name__ == "__main__":    
    app.run(host="127.0.0.1", port=5005, debug=True)
