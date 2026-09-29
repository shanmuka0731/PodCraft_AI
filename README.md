# 🎙️ PodCraft_AI - Blog to Podcast

Blog to Podcast is an AI-powered application that transforms a blog article into a natural two-speaker podcast conversation.

The application extracts an article from a URL, uses an LLM to analyze and transform the content into a podcast script, assigns the conversation to a HOST and EXPERT, converts each speaker's dialogue into speech using Piper TTS, and combines the audio into a single downloadable podcast.

---

## ✨ Features

- 🔗 Extract article content directly from a URL
- 🤖 AI-powered article analysis and podcast generation
- 📝 Generates a natural HOST–EXPERT conversation
- 🎙️ Separate voices for HOST and EXPERT
- 🔊 Local text-to-speech using Piper TTS
- 🎧 Combines multiple speech segments into one podcast
- ⬇️ Download the generated podcast as a WAV file
- 🌙 Clean dark-themed Streamlit interface
- 🔐 API keys stored securely using environment variables

---
## 🛠️ Tech Stack
- Python - Core application
- Streamlit - Web interface
- Groq - LLM inference
- GPT-OSS-20B - Podcast script generation
- Newspaper4k - Article extraction
- Piper - TTS	Local text-to-speech
- Git & GitHub - Version control

---

## 1. Clone the Repository
- git clone https://github.com/shanmuka0731/AI-Blog-to-Podcast.git
## 2. Open the Project Folder
cd AI-Blog-to-Podcast
## 3. Create a Virtual Environment
python -m venv .venv
## 4. Activate it
.venv\Scripts\activate
## 5. Install Dependencies
pip install -r requirements.txt
## 6. Configure the Groq API Key
Create a .env file in the project root:

GROQ_API_KEY=your_groq_api_key_here
## 7. Install Piper TTS
pip install piper-tts
## 8. Download the required voice model:
python -m piper.download_voices en_US-lessac-medium

- Place the downloaded voice files inside the voices/ directory.
## 9. Run the Application
streamlit run app.py

---

## 🔮 Future Improvements

- 🎚️ Adjustable podcast length

- 🎙️ More voice options

- ⚡ Reduce the number of LLM calls

- 📱 Improved responsive UI

- 🎵 Background music

- ⏱️ Podcast duration estimation

- 🧹 Automatic cleanup of temporary audio segments

---

## 👩‍💻 Author

Shanmuka Priya Salapu

---

## 🎯 Project Goal

The goal of this project is to explore how LLMs, AI workflows, web scraping, text-to-speech, and audio processing can be combined to create an end-to-end AI application.


## 📄 License

This project is intended for educational and portfolio purposes.


