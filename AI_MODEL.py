import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Define your training data (Keywords and related concepts)
training_data = [
    {"keywords": "hello hi hey greetings welcome", "response": "Hello! Welcome to our canteen."},
    {"keywords": "price cost money rupees pizza", "response": "Pizza costs ₹120."},
    {"keywords": "time open close working hours shut", "response": "The canteen is open 8 AM to 6 PM."},
    {"keywords": "menu today food items dish serve", "response": "Today's menu includes Pizza and Coffee."}
]

df = pd.DataFrame(training_data)

# 2. Train the model
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['keywords'])

def get_ai_response(user_input):
    # Transform user input into the trained vector space
    user_vec = vectorizer.transform([user_input.lower()])
    
    # Calculate similarity score between input and training data
    similarities = cosine_similarity(user_vec, tfidf_matrix)
    
    # Find the highest matching score
    best_match_idx = similarities.argmax()
    max_similarity = similarities[0, best_match_idx]
    
    # 3. Set a threshold to handle unknown questions
    if max_similarity > 0.1:
        return df.iloc[best_match_idx]['response']
    else:
        return "Sorry, I didn't understand that. Could you rephrase?"

# 4. Test the chatbot with phrases missing exact terms
print("User: When do you guys shut down?")
print("Bot:", get_ai_response("When do you guys shut down?"))

print("\nUser: How much cash for a slice?")
print("Bot:", get_ai_response("How much cash for a slice?"))