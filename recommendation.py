from flask import Flask, request, jsonify
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

def recommendationSyst(user_preferences, item_features, num_recommendations=5):

    user_vector = np.zeros((1, len(item_features[list(item_features.keys())[0]])))
    for item, rating in user_preferences.items():
        if item in item_features:
            user_vector += rating * np.array(item_features[item]).reshape(1, -1)
    
    features = np.array(list(item_features.values()))
    
    similarities = cosine_similarity(user_vector, features)
    
    sorted_indices = np.argsort(similarities)[0][::-1]
    
    recommendations = []
    for i in range(min(num_recommendations, len(sorted_indices))):
        index = sorted_indices[i]
        recommendations.append(list(item_features.keys())[index])
    
    return recommendations

@app.route('/recommend', methods=['POST'])
def recommend():
    request_data = request.get_json()
    user_preferences = request_data['user_preferences']
    item_features = request_data['item_features']
    num_recommendations = request_data.get('num_recommendations', 5)
    recommendations = recommendationSyst(user_preferences, item_features, num_recommendations)
    return jsonify({'recommendations': recommendations})

if __name__ == '__main__':
    app.run(debug=True)
