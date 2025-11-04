from flask import Flask, request, jsonify
from flask_cors import CORS
from flux_bot import get_bot_response  # <-- Imports our logic from the other file

# Initialize the Flask app
app = Flask(__name__)

# Enable CORS (Cross-Origin Resource Sharing)
CORS(app)

# Define the API endpoint
@app.route("/chat", methods=["POST"])
def chat():
    try:
        # Get the user's message from the incoming JSON request
        user_message = request.json["message"]
        
        # Check if the message is empty
        if not user_message:
            return jsonify({"reply": "Please send a message."}), 400

        # Get the bot's reply using our imported logic
        bot_reply = get_bot_response(user_message)
        
        # Return the bot's reply as a JSON response
        return jsonify({"reply": bot_reply})

    except KeyError:
        # This error happens if the JSON payload doesn't have a "message" key
        return jsonify({"error": "Missing 'message' key in request."}), 400
    except Exception as e:
        # Catch any other potential errors
        print(f"An error occurred: {e}")
        return jsonify({"error": "An internal server error occurred."}), 500

# This part is optional for `flask run` but good practice
if __name__ == "__main__":
    app.run(debug=True)