import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()   # read .env file and load environment variables
api_key =  os.getenv("GROQ_API_KEY")  


def build_prompt(metadata, transcript):
    return f"""
You are a YouTube content expert.

VIDEO METADATA:
- Title: {metadata.get('Title', 'Unknown')}
- Author: {metadata.get('Author', 'Unknown')}
- Views: {metadata.get('views', 'Unknown')}
- Description: {metadata.get('Description', 'Unknown')}

Video TRANSCRIPT:
{transcript}

TASKS:

1. Generate 5 catchy YouTube titles optimized for high click-through rates (CTR).
2. Write one SEO optimized description (max 200 words)
3. Suggest 3 thumbnails ideas (describe visuals and text)

Respond with clear sections:
Titles:
Descriptions:
Thumbnails:
"""

def analyze_video(metadata, transcript):
    if api_key is None:
        print("API key not found!")
        return None
    
    client = Groq(api_key=api_key)
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": build_prompt(metadata, transcript)}
            ]
        )
        return response.choices[0].message.content

    except Exception as e:
        print(f"Error calling Groq API: {e}")
        return None


if __name__ == "__main__":
    # Fake data just for testing this file
    test_metadata = {
        "Title": "How to Learn Python Fast",
        "Author": "TechChannel",
        "views": 150000,
        "Description": "A beginner guide to Python..."
    }
    test_transcript = "In this video I will teach you Python basics..."

    result = analyze_video(test_metadata, test_transcript)
    print(result)