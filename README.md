# Customer-Support-Chatbot

# AI-Powered Customer Support Chatbot

---

## Project Overview

This project implements an AI-powered chatbot designed to automate customer support for common queries related to products, orders, returns, payments, and warranties. It uses a Retrieval-Augmented Generation (RAG) approach, combining semantic search over FAQs with Large Language Models (LLMs) to provide accurate, context-aware, multi-turn conversational responses.

---

## Features

- Semantic similarity search using SentenceTransformers and FAISS.
- Contextual, multi-turn conversation support.
- Response generation with local LLMs (via Ollama) or Hugging Face models.
- Simple Streamlit-based web interface.
- Robust handling of ambiguous, multi-part, or misspelled queries.
- Easily extendable FAQ dataset stored in JSON files.

---

## Technology Stack

- **Frontend:** Streamlit
- **Embedding Model:** sentence-transformers/all-mpnet-base-v2
- **Vector Search:** FAISS
- **Language Model:** Mistral-7B-Instruct (via Ollama or Hugging Face)
- **Data Storage:** JSON files for FAQs and FAISS index
- **Session Management:** Streamlit session state for maintaining conversation history

---

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ai-customer-support-chatbot.git
   cd ai-customer-support-chatbot

