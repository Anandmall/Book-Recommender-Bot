import streamlit as st
import requests

# API base URL
API_BASE_URL = "http://localhost:3000/books"

# Streamlit app
st.title("Book Recommender Chatbot")

# Initialize session state for conversation flow
if 'step' not in st.session_state:
    st.session_state.step = "initial"
if 'criteria' not in st.session_state:
    st.session_state.criteria = None
if 'query' not in st.session_state:
    st.session_state.query = ""


# Function to fetch recommendations
def fetch_recommendations(criteria, query):
    try:
        response = requests.get(f"{API_BASE_URL}/{criteria}?q={query}")
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return None


# Initial greeting
if st.session_state.step == "initial":
    st.write("Welcome, how can I assist you?")
    if st.button("Get Book Recommendations"):
        st.session_state.step = "select_criteria"

# Select recommendation criteria
if st.session_state.step == "select_criteria":
    st.write("Sure! I can help you find a book. Would you like recommendations based on genre, author, or your mood?")
    criteria = st.selectbox("Choose an option:", ["", "genre", "author", "mood"], index=0)
    if criteria and st.button("Next"):
        st.session_state.criteria = criteria
        st.session_state.step = f"input_{criteria}"

# Input for genre
if st.session_state.step == "input_genre":
    st.write("What genre are you interested in? Ex: Mystery, Romance, Sci-Fi, Fantasy, Thriller, or something else?")
    genre = st.text_input("Enter genre:")
    if genre and st.button("Get Recommendations"):
        st.session_state.query = genre
        books = fetch_recommendations("genre", genre)
        if books:
            for book in books:
                st.markdown(
                    f"**Title**: *{book['title']}*  \n**Author**: {book['author']}  \n**Description**: {book['description']}")
        else:
            st.write("Sorry, I couldn't fetch book recommendations at this time. Please try again later.")
        st.session_state.step = "done"

# Input for author
if st.session_state.step == "input_author":
    st.write("Who’s your favorite author or one you’ve enjoyed recently?")
    author = st.text_input("Enter author:")
    if author and st.button("Get Recommendations"):
        st.session_state.query = author
        books = fetch_recommendations("author", author)
        if books:
            for book in books:
                st.markdown(
                    f"**Title**: *{book['title']}*  \n**Author**: {book['author']}  \n**Description**: {book['description']}")
        else:
            st.write("Sorry, I couldn't fetch book recommendations at this time. Please try again later.")
        st.session_state.step = "done"

# Input for mood
if st.session_state.step == "input_mood":
    st.write(
        "Got it! How are you feeling right now? I can suggest books based on your mood. (Examples: happy, sad, "
        "stressed, adventurous, romantic, curious, etc.)")
    mood = st.text_input("Enter mood:")
    if mood and st.button("Get Recommendations"):
        st.session_state.query = mood
        books = fetch_recommendations("mood", mood)
        if books:
            for book in books:
                st.markdown(
                    f"**Title**: *{book['title']}*  \n**Author**: {book['author']}  \n**Description**: {book['description']}")
        else:
            st.write("Sorry, I couldn't fetch book recommendations at this time. Please try again later.")
        st.session_state.step = "done"

# Reset option
if st.session_state.step == "done":
    if st.button("Start Over"):
        st.session_state.step = "initial"
        st.session_state.criteria = None
        st.session_state.query = ""
