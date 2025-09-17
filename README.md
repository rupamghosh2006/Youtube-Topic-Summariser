# 🎥 YouTube Topic Summarizer with Gemini + Flask

This project provides a simple **Flask API** that:
1. Fetches **YouTube videos** about a given topic.
2. Uses **Google Gemini** to generate a **concise summary** of the main themes, trends, and insights.
3. Returns both the **summary** and the **video details** in JSON.

---

## 🚀 Features
- 🔍 Search YouTube videos by topic (via [`youtubesearchpython`](https://github.com/alexmercerind/youtube-search-python)).
- 🤖 Summarize results using **Google Gemini 1.5 Flash**.
- 🌐 REST API with **GET** and **POST** endpoints.
- 🔑 Secure API key management with `.env`.

---

## 📂 Project Structure
```bash
├── app.py              # Flask API routes
├── youtube_search.py   # YouTube search helper
├── gemini_use.py       # Gemini summarization logic
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
