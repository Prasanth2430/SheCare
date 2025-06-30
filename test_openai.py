#!/usr/bin/env python3
"""
Test script to verify OpenAI API connection
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

def test_openai_connection():
    """Test the OpenAI API connection"""
    
    # Load environment variables
    load_dotenv()
    
    # Get API key
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        print("❌ Error: OPENAI_API_KEY not found in .env file")
        return False
    
    if api_key.startswith("sk-"):
        print("✅ OpenAI API key found in .env file")
    else:
        print("⚠️  Warning: API key format might be incorrect")
    
    try:
        # Initialize OpenAI client
        client = OpenAI(api_key=api_key)
        
        # Test with a simple request
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Say hello!"}
            ],
            max_tokens=50
        )
        
        print("✅ OpenAI API connection successful!")
        print(f"Response: {response.choices[0].message.content}")
        return True
        
    except Exception as e:
        print(f"❌ Error connecting to OpenAI API: {str(e)}")
        return False

if __name__ == "__main__":
    print("Testing OpenAI API connection...")
    print("=" * 40)
    test_openai_connection()
