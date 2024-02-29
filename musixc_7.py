import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Sample music data (user-item matrix)
music_data = {
    'User': ['User1', 'User2', 'User3', 'User4', 'User5'],
    'Pop': [5, 8, 0, 0, 3],
    'Classical': [0, 5, 3, 1, 1],
    'Rock': [0, 1, 5, 4, 0],
    'Hip-Hop': [2, 0, 2, 0, 5],
    'Country': [0, 0,0, 5, 0],
}

# Convert data to DataFrame
df = pd.DataFrame(music_data)

# Calculate similarity matrix using cosine similarity
similarity_matrix = cosine_similarity(df.drop('User', axis=1))

# Function to recommend tracks for a given user
def recommend_tracks(user_id, similarity_matrix, num_recommendations=3):
    user_index = df[df['User'] == user_id].index[0]
    user_similarities = similarity_matrix[user_index]
    similar_users_indices = user_similarities.argsort()[-num_recommendations-1:-1][::-1]  # Exclude user's own index
    recommended_tracks = []
    for index in similar_users_indices:
        similar_user_id = df.iloc[index]['User']
        user_tracks = df.iloc[index][1:]
        recommended_tracks.extend(user_tracks[user_tracks > 0].index)  # Only recommend tracks with rating > 0
    return list(set(recommended_tracks))[:num_recommendations]  # Remove duplicates and limit recommendations


user_id1 = 'User1'
recommended_tracks = recommend_tracks(user_id1, similarity_matrix)
print("These are the recommended tracks for", user_id1, ":", recommended_tracks)
