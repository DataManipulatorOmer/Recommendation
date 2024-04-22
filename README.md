# Recommendation System API

## Introduction
This repository contains a simple Flask API for a recommendation system. The recommendation system generates personalized recommendations based on user preferences and item features using cosine similarity.

## How to Use

1. Run the Flask app:
    ```bash
    python app.py
    ```

2. Send a POST request to the `/recommend` endpoint with JSON data containing user preferences and item features. You can use tools like Postman for testing.

    Example JSON data:
    ```json
    {
        "user_preferences": {
            "popularity": 0.7,
            "price": 0.9,
            "brand": 0.3
        },
        "item_features": {
            "Item1": [0.8, 0.5, 0.2],
            "Item2": [0.6, 0.7, 0.4],
            "Item3": [0.3, 0.9, 0.1],
            "Item4": [0.1, 0.4, 0.6]
        },
        "num_recommendations": 5
    }
    ```

3. Receive recommended items based on the user preferences.

