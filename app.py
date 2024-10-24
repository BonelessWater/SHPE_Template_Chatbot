from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os
from prompt import prompt

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# i.e The route is https://localhost:5000/api/greet
@app.route('/api/greet', methods=['POST'])
def greet():
    pass
    # Work here


def response(topic):
    # Fetches API key from the .env file
    

    # Send an API call to OpenAI to generate a response
    

    # Awaits chatgpt for its response
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        # Sets the mood for how to respond to user propmt
        {"role": "system", "content": prompt}, 

        # Takes the topic from the user and passes it as a prompt to chatgpt
        {"role": "user", "content": f"Tell me everything you know about this topic: {topic}" }
    ]
    )
    
    # Returns the part of the dictionary that only contains the text
    return response.choices[0].message.content

if __name__ == '__main__':
    app.run(port=5000, debug=True) # Runs on port 5000 by default
