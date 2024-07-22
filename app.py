from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)  # Allow CORS for all origins during development

# Set the API key for Google Generative AI
api_key = "YOUR_API_KEY"
genai.configure(api_key=api_key)

BOT_NAME = "YOUR_BOT_NAME"

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
}

# Initialize the Generative AI model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Initial context for the conversation
initial_context = """<INSERT_HERE>""" #Based on this context the bot is going to proceed with the conversation, It can be left empty or Filled with constrains

def generate_response(user_message):
    try:
        # Combine initial context with user message
        combined_message = f"{initial_context}\nUser: {user_message}\n{BOT_NAME}:"
        
        # Generate content based on the combined message
        result = model.generate_content([combined_message])
        
        if result and result.candidates:
            # Assuming we want the first candidate's content as text
            return result.candidates[0].content.parts[0].text.strip()
        else:
            return "No response from the model."
    except Exception as e:
        return f"Error generating response: {str(e)}"

@app.route('/chat', methods=['POST'])
def chat():
    try: 
        data = request.get_json()
        user_message = data.get('message')

        if not user_message:
            return jsonify({'response': 'No message provided'}), 400

        # Generate bot response using Generative AI model
        bot_response = generate_response(user_message)

        return jsonify({'response': bot_response}), 200

    except Exception as e:
        return jsonify({'response': f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)

