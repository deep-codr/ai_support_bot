from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.utils.text_cleaner import clean_text
import numpy as np

def find_best_match(user_input_, intents_data):
    user_input = clean_text(user_input_)

    all_patterns = []
    tags = []

    for intent in intents_data['intents']:
        for pattern in intent['patterns']:
            all_patterns.append(clean_text(pattern))
            tags.append(intent['tag'])
    
    # TF-IDF Vectorize
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(all_patterns + [user_input])

    # Last vecctor is user-input
    user_vec = vectors[-1]
    pattern_vecs = vectors[:-1]

    # Cosine similarity
    similarity = cosine_similarity(user_vec, pattern_vecs)

    # Best match 
    best_match_index = np.argmax(similarity)
    best_tag = tags[best_match_index]
    best_score = similarity[0][best_match_index]

    # Thresold (Optional)
    if best_score < 0.3:
        return "I'm sorry, I couldn't understand that. Could you rephrase?"
    
    # Return response
    for intent in intents_data['intents']:
        if intent['tag'] == best_tag:
            return np.random.choice(intent['responses'])
        