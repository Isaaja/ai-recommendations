from flask import Flask, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
# Load dataset
df = pd.read_csv("./movie_data.csv")

# TF-IDF Vectorizer untuk genre
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(df['genres_id'].fillna(''))

# Hitung Cosine Similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Fungsi rekomendasi berdasarkan id
def recommend_anime(id, top_n=10):
    if id not in df['id'].values:
        return []

    index = df[df['id'] == id].index[0]
    sim_scores = list(enumerate(cosine_sim[index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]

    anime_indices = [i[0] for i in sim_scores]
    recommended_anime = df.iloc[anime_indices].sort_values(by='vote_average', ascending=False)

    return recommended_anime[['id', 'original_title', 'genres_id', 'vote_average']].to_dict(orient='records')

# API Endpoint untuk rekomendasi
@app.route('/recommend', methods=['GET'])
def recommend():
    id = request.args.get('id')
    if not id:
        return jsonify({"error": "Masukkan parameter id"}), 400
    
    try:
        id = int(id)
    except ValueError:
        return jsonify({"error": "id harus berupa angka"}), 400

    recommendations = recommend_anime(id)
    if not recommendations:
        return jsonify({"error": "Anime tidak ditemukan"}), 404

    return jsonify({"recommendations": recommendations})

if __name__ == '__main__':
    app.run(debug=True)