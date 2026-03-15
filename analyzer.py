import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()   # read .env file and load environment variables
api_key =  os.getenv("GROQ_API_KEY")  


def build_prompt(metadata, transcript):
    return f"""
You are a YouTube content expert.

Here is a YouTube video:
- Title: {metadata['Title']}
- Author: {metadata['Author']}
- Views: {metadata['views']}
- Description: {metadata['Description']}

Transcript:
{transcript}

Please provide:
1. Five catchy title suggestions
2. One optimized description (max 200 words)
3. Three thumbnail ideas (describe visuals)
"""

def analyze_video(metadata, transcript):
    if api_key is None:
        print("API key not found!")
        return None
    
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": build_prompt(metadata, transcript)}
        ]
    )
    return response.choices[0].message.content


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