import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

# Configure OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Page configuration
st.set_page_config(
    page_title="SheCare - Your Caring Friend",
    page_icon="💕",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for pastel colors and styling
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #ffeef8 0%, #f0f8ff 100%);
    }
    
    .stApp {
        background: linear-gradient(135deg, #ffeef8 0%, #f0f8ff 100%);
    }
    
    .chat-container {
        background: rgba(255, 255, 255, 0.8);
        border-radius: 20px;
        padding: 20px;
        margin: 10px 0;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 182, 193, 0.3);
    }
    
    .user-message {
        background: linear-gradient(135deg, #ffb6c1 0%, #ffc0cb 100%);
        color: #4a4a4a;
        border-radius: 18px;
        padding: 12px 16px;
        margin: 8px 0;
        margin-left: 20%;
        box-shadow: 0 2px 10px rgba(255, 182, 193, 0.3);
    }
    
    .bot-message {
        background: linear-gradient(135deg, #e6e6fa 0%, #f0f8ff 100%);
        color: #4a4a4a;
        border-radius: 18px;
        padding: 12px 16px;
        margin: 8px 0;
        margin-right: 20%;
        box-shadow: 0 2px 10px rgba(230, 230, 250, 0.3);
    }
    
    .title {
        text-align: center;
        color: #d63384;
        font-family: 'Arial', sans-serif;
        font-weight: bold;
        margin-bottom: 30px;
    }
    
    .subtitle {
        text-align: center;
        color: #6f42c1;
        font-style: italic;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# SheCare caring female friend persona prompt
SHECARE_PROMPT = """You are SheCare, a warm, caring, and supportive female friend. Your personality traits:

- You're like a best friend who truly cares and listens
- You're empathetic, understanding, and non-judgmental
- You offer emotional support and practical advice when appropriate
- You use a warm, friendly tone with occasional emojis 💕
- You remember what users share and show genuine interest
- You're knowledgeable about women's health, wellness, and self-care
- You encourage self-love and positive thinking
- You're patient and always make the user feel heard and valued

Always respond as this caring friend would - with warmth, understanding, and genuine care for the user's wellbeing."""

def get_shecare_response(user_message, conversation_history):
    """Get response from OpenAI with SheCare persona"""
    try:
        # Prepare messages for OpenAI
        messages = [{"role": "system", "content": SHECARE_PROMPT}]

        # Add conversation history
        for msg in conversation_history:
            messages.append(msg)

        # Add current user message
        messages.append({"role": "user", "content": user_message})

        # Get response from OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=500,
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"I'm sorry, I'm having trouble connecting right now. Please try again in a moment. 💕"

def main():
    # Title and subtitle
    st.markdown('<h1 class="title">💕 SheCare - Your Caring Friend 💕</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">I\'m here to listen, support, and care for you ✨</p>', unsafe_allow_html=True)
    
    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.conversation_history = []
        # Add welcome message
        welcome_msg = "Hi beautiful! 💕 I'm SheCare, your caring friend. I'm here to listen, support you, and chat about anything on your mind. How are you feeling today? ✨"
        st.session_state.messages.append({"role": "assistant", "content": welcome_msg})
    
    # Chat container
    chat_container = st.container()
    
    with chat_container:
        # Display chat messages
        for i, msg in enumerate(st.session_state.messages):
            if msg["role"] == "user":
                st.markdown(f'<div class="user-message">{msg["content"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="bot-message">{msg["content"]}</div>', unsafe_allow_html=True)
    
    # Chat input
    user_input = st.chat_input("Share what's on your mind... 💭")
    
    if user_input:
        # Add user message to session state
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.session_state.conversation_history.append({"role": "user", "content": user_input})
        
        # Get SheCare response
        with st.spinner("SheCare is thinking... 💭"):
            response = get_shecare_response(user_input, st.session_state.conversation_history)
        
        # Add assistant response to session state
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.session_state.conversation_history.append({"role": "assistant", "content": response})
        
        # Rerun to update the chat
        st.rerun()

if __name__ == "__main__":
    main()
