import streamlit as st
import requests
import sys
from pathlib import Path

# Allow importing modules from the project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

# Backend API URL
BASE_URL = "http://127.0.0.1:8000"

# Configure Streamlit page
st.set_page_config(
    page_title="Personalized Networking Assistant",
    page_icon="🤝",
    layout="wide"
)

# Application Title
st.title("🤝 Personalized Networking Assistant")
st.write(
    "Generate personalized conversation starters for networking events, "
    "verify facts, and review your previous interactions."
)
st.markdown("---")

st.header("📝 Generate Conversation Starters")

event_description = st.text_area(
    "Event Description",
    placeholder="Example: AI for Sustainable Cities"
)

user_interests = st.text_input(
    "Your Interests (comma separated)",
    placeholder="AI, Machine Learning, Sustainability"
)
if st.button("🚀 Generate Conversation Starters"):

    if event_description.strip() == "":
        st.warning("Please enter an event description.")

    else:

        interests = [
            interest.strip()
            for interest in user_interests.split(",")
            if interest.strip()
        ]

        payload = {
            "description": event_description,
            "interests": interests
        }

        response = requests.post(
            f"{BASE_URL}/generate-conversation",
            json=payload
        )

        if response.status_code == 200:

            data = response.json()

            st.session_state["themes"] = data["themes"]
            st.session_state["suggestions"] = data["suggestions"]

        else:
            st.error("Unable to generate conversation starters.")
if "suggestions" in st.session_state:

    st.markdown("---")

    st.subheader("🎯 Extracted Themes")

    for theme in st.session_state["themes"]:
        st.write(f"✅ {theme}")

    st.markdown("---")

    st.subheader("💬 Conversation Starters")

    for i, suggestion in enumerate(st.session_state["suggestions"]):

        st.success(suggestion)

        col1, col2 = st.columns(2)

        # Like button
        if col1.button("👍 Like", key=f"like_{i}"):

            feedback_payload = {
                "suggestion": suggestion,
                "action": "like"
            }

            requests.post(
                f"{BASE_URL}/feedback",
                json=feedback_payload
            )

            st.toast("Thanks for your feedback 👍")

        # Dislike button
        if col2.button("👎 Dislike", key=f"dislike_{i}"):

            feedback_payload = {
                "suggestion": suggestion,
                "action": "dislike"
            }

            requests.post(
                f"{BASE_URL}/feedback",
                json=feedback_payload
            )

            st.toast("Feedback recorded 👎")
st.markdown("---")

st.header("🔎 Fact Check Anything")

fact_query = st.text_input(
    "Enter topic to verify",
    placeholder="Example: Blockchain in Healthcare"
)

if st.button("Check Fact"):

    if fact_query.strip() == "":
        st.warning("Please enter a topic to fact check.")

    else:

        response = requests.post(
            f"{BASE_URL}/fact-check",
            json={"query": fact_query}
        )

        if response.status_code == 200:

            data = response.json()
            st.success(data["result"])

        else:
            st.error("Fact check failed.")
import json
from pathlib import Path

st.markdown("---")
st.header("📜 Recent Conversation History")

history_file = Path("data/history.json")

if history_file.exists():

    with open(history_file, "r") as f:
        history = json.load(f)

    recent_history = history[-5:]

    if recent_history:
        for item in reversed(recent_history):

            st.subheader(item["description"])

            st.write("**Themes:**")
            for theme in item["themes"]:
                st.write(f"- {theme}")

            st.write("**Conversation Starters:**")
            for suggestion in item["suggestions"]:
                st.write(f"- {suggestion}")

            st.markdown("---")

    else:
        st.info("No conversation history found.")

else:
    st.info("History file not found.")
st.markdown("---")
st.header("👍 Feedback History")

feedback_file = Path("data/feedback.json")

if feedback_file.exists():

    with open(feedback_file, "r") as f:
        feedback = json.load(f)

    recent_feedback = feedback[-10:]

    if recent_feedback:

        for item in reversed(recent_feedback):

            icon = "👍" if item["action"] == "like" else "👎"

            st.write(f"{icon} {item['suggestion']}")

            if "timestamp" in item:
                st.caption(item["timestamp"])

            st.markdown("---")

    else:
        st.info("No feedback available.")

else:
    st.info("Feedback file not found.")         