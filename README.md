# Personalized Networking Assistant 🤝

An AI-powered networking assistant that helps users prepare meaningful conversations before attending professional events. The application analyzes an event description, identifies key themes using AI, generates personalized conversation starters based on the user's interests, verifies facts using Wikipedia, and stores conversation and feedback history.

---

## 📌 Features

* 🔍 AI-based event theme extraction
* 💬 Personalized conversation starter generation
* 📖 Wikipedia-powered fact checking
* 📝 Conversation history logging
* 👍 User feedback collection
* 🌐 FastAPI REST APIs
* 🎨 Streamlit web interface
* ✅ Automated unit and API testing using Pytest

---

## 🛠️ Tech Stack

### Backend

* Python
* FastAPI
* Uvicorn

### AI & NLP

* Hugging Face Transformers
* Facebook BART Large MNLI (Zero-Shot Classification)

### Frontend

* Streamlit

### Data Storage

* JSON Files

### Testing

* Pytest
* FastAPI TestClient

---

## 📂 Project Structure

```text
Personalized-Networking-Assistant/
│
├── app/
│   ├── models/
│   ├── routers/
│   ├── services/
│   ├── main.py
│   └── __init__.py
│
├── frontend/
│   └── streamlit_app.py
│
├── data/
│   ├── history.json
│   └── feedback.json
│
├── tests/
│   ├── test_event_analyzer.py
│   ├── test_topic_generator.py
│   ├── test_fact_checker.py
│   └── test_api.py
│
├── requirements.txt
├── README.md
└── main.py
```
## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Personalized-Networking-Assistant.git
cd Personalized-Networking-Assistant
```

### 2. Create a Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Start the FastAPI Backend

```bash
uvicorn app.main:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

Swagger API documentation:

```text
http://127.0.0.1:8000/docs
```

---

### Start the Streamlit Frontend

Open a second terminal and run:

```bash
streamlit run frontend/streamlit_app.py
```

The application will open automatically in your browser at:

```text
http://localhost:8501
```

---

## 🧪 Running Tests

Run all tests:

```bash
pytest -v
```

Run tests with coverage:

```bash
pytest --cov=app
```

---

## 📡 API Endpoints

| Method | Endpoint                 | Description                        |
| ------ | ------------------------ | ---------------------------------- |
| GET    | `/`                      | Health check                       |
| POST   | `/analyze-event`         | Extract event themes               |
| POST   | `/generate-conversation` | Generate conversation starters     |
| POST   | `/fact-check`            | Verify information using Wikipedia |
| POST   | `/feedback`              | Save user feedback                 |

---

## 📈 Future Enhancements

* Add user authentication.
* Store data in a database such as PostgreSQL or MongoDB.
* Support multiple languages.
* Integrate Large Language Models for richer conversation suggestions.
* Deploy using Docker and a cloud platform such as AWS or Azure.

---

## 👩‍💻 Author

**Usha Sri**

B.Tech – Computer Science & Engineering

This project was developed as an AI-powered networking assistant to demonstrate practical skills in FastAPI, Streamlit, NLP, REST API development, and software testing.
