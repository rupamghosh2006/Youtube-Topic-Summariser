from flask import Flask, request, jsonify
from youtube_search import search_youtube
from gemini_use import summarize_with_gemini
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

@app.route("/youtube-summary", methods=["GET"])
def youtube_summary_get():
    topic = request.args.get("topic")
    limit = int(request.args.get("limit", 5))

    if not topic:
        return jsonify({"error": "Please provide a topic"}), 400

    videos = search_youtube(topic, limit)
    if not videos:
        return jsonify({"error": "No videos found"}), 404

    summary = summarize_with_gemini(videos)
    return jsonify({"topic": topic, "summary": summary, "videos": videos})

@app.route("/youtube-summary", methods=["POST"])
def youtube_summary_post():
    data = request.get_json()
    topic = data.get("topic")
    limit = int(data.get("limit", 5))

    if not topic:
        return jsonify({"error": "Please provide a topic"}), 400

    videos = search_youtube(topic, limit)
    if not videos:
        return jsonify({"error": "No videos found"}), 404

    summary = summarize_with_gemini(videos)
    return jsonify({"topic": topic, "summary": summary, "videos": videos})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)