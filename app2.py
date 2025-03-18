from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load sentiment analysis model
sentiment_pipeline = pipeline("sentiment-analysis")

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    review_text = data.get('text')

    if not review_text:
        return jsonify({"error": "No review text provided"}), 400

    result = sentiment_pipeline(review_text)

    return jsonify({
        "sentiment": result[0]["label"],
        "confidence": result[0]["score"]
    })

if __name__ == '__main__':
    app.run(debug=True)
