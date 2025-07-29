from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def find_best_match(query, faq_df):
    questions = faq_df['question'].fillna('').tolist()
    answers = faq_df['answer'].fillna('').tolist()

    vectorizer = TfidfVectorizer()
    Tfidf_matrix = vectorizer.fit_transform(questions + [query])

    similarities = cosine_similarity(Tfidf_matrix[-1], Tfidf_matrix[:-1])
    best_idx = similarities.argmax()
    score = similarities[0, best_idx]

    if score > 0.5:
        return {'question': questions[best_idx], 'answer': answers[best_idx]}
    else:
        return None