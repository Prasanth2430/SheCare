# SheCare - Your Caring Friend Chatbot 💕

A Streamlit-based chatbot with a caring female friend persona, designed to provide emotional support and companionship.

## Features

- 💕 Caring female friend persona
- 🎨 Beautiful pastel-colored UI with chat bubbles
- 🤖 OpenAI GPT-3.5 integration
- 💬 Real-time chat interface
- 🌸 Responsive and mobile-friendly design

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Make sure your `.env` file contains your OpenAI API key:

```
OPENAI_API_KEY=your_openai_api_key_here
```

### 3. Test OpenAI Connection (Optional)

```bash
python test_openai.py
```

### 4. Run the Application

**Option 1: Using Python module**

```bash
python -m streamlit run app.py
```

**Option 2: Using the batch file (Windows)**

```bash
run_shecare.bat
```

**Option 3: Direct streamlit command (if in PATH)**

```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501`

## Usage

1. Open the application in your browser
2. Start chatting with SheCare - your caring friend
3. Share your thoughts, feelings, or ask for advice
4. Enjoy the supportive and caring conversation

## Technologies Used

- **Streamlit** - Web application framework
- **OpenAI GPT-3.5** - AI conversation model
- **Python** - Backend programming language
- **CSS** - Custom styling for pastel colors and chat bubbles

## Persona

SheCare is designed to be:

- Warm, caring, and supportive
- A good listener who shows genuine interest
- Empathetic and non-judgmental
- Knowledgeable about wellness and self-care
- Encouraging and positive

Enjoy your conversations with SheCare! 💕✨
