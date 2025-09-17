import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def load_vector_store():
    try:
        with open('vector_store/faiss_index.pkl', 'rb') as f:
            index, faqs = pickle.load(f)
        return index, faqs
    except Exception as e:
        raise FileNotFoundError("Vector store loading failed. Details: " + str(e))

def search_similar_question(query, index, faqs, top_k=1, threshold=3.0):
    query_vec = model.encode([query])
    distances, indices = index.search(np.array(query_vec), top_k)

    if distances[0][0] < threshold:
        matched_faq = faqs[indices[0][0]]
        return matched_faq['question'], matched_faq['answer']
    
    return None, "Sorry, I couldn't find a relevant answer in our FAQ database."
