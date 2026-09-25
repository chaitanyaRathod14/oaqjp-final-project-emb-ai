"""Flask web server for the EmotionDetection project."""

from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector


app = Flask(__name__)


@app.route("/")
def index():
    """Render the emotion detection form."""
    return render_template("index.html")


@app.route("/emotionDetector")
def detect_emotion():
    """Analyze the text supplied by the browser."""
    text_to_analyze = request.args.get("textToAnalyze", "")
    if not text_to_analyze.strip():
        return "Invalid input! Try again!", 400

    result = emotion_detector(text_to_analyze)
    if result["dominant_emotion"] is None:
        return "Emotion service unavailable. Try again later.", 502

    return (
        "For the given statement, the system response is: "
        f"anger: {result['anger']}, "
        f"disgust: {result['disgust']}, "
        f"fear: {result['fear']}, "
        f"joy: {result['joy']}, "
        f"sadness: {result['sadness']}, "
        f"dominant_emotion: {result['dominant_emotion']}"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
