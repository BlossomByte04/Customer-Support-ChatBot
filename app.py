import streamlit as st
from utils import load_vector_store, search_similar_question
import subprocess

# App config
st.set_page_config(page_title="Customer Support Chatbot", page_icon="🛍️")
st.title("🛍️ E-commerce Customer Support Chatbot")

# Load vector store
try:
    index, faqs = load_vector_store()
except FileNotFoundError:
    st.error("Vector store not found. Please run embed_faqs.py first.")
    st.stop()

# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Chat input
user_input = st.chat_input("Ask me anything about your order, warranty, returns, etc.")

if user_input:
    # Add user's message to chat history
    st.session_state.history.append(("user", user_input))

    # Search FAQ vector store
    retrieved_q, context = search_similar_question(user_input, index, faqs)

    # Build prompt for LLM
    prompt = ""
    for role, message in st.session_state.history:
        prompt += f"{role.capitalize()}: {message}\n"
    if context:
        prompt += f"Context: {context}\n"
    prompt += "Assistant:"

    # Run local LLM via Ollama
    try:
        result = subprocess.run(
            ["ollama", "run", "mistral"],
            input=prompt,
            capture_output=True,
            text=True,
            check=True
        )
        bot_response = result.stdout.strip()
    except Exception as e:
        bot_response = "Sorry, I'm having trouble generating a response right now."

    # Add bot's response to chat history
    st.session_state.history.append(("assistant", bot_response))

# Display the chat messages
for role, message in st.session_state.history:
    with st.chat_message(role):
        st.markdown(message)
