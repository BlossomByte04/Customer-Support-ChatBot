import json
import faiss
import pickle
import os
import numpy as np
from sentence_transformers import SentenceTransformer

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load FAQs
with open('faqs.json', 'r') as f:
    faqs = json.load(f)

questions = [faq['question'] for faq in faqs]

# Create embeddings
embeddings = model.encode(questions, show_progress_bar=True)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

# Ensure directory exists
os.makedirs("vector_store", exist_ok=True)

# Save index and FAQs
with open('vector_store/faiss_index.pkl', 'wb') as f:
    pickle.dump((index, faqs), f)

print("Vector store created and saved.")
