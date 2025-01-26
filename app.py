import logging
import time
import os
from flask import Flask, request, jsonify

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# Endpoint to activate the application
@app.route('/activate', methods=['POST'])
def activate():
    data = request.json
    if not data or 'message' not in data:
        logger.warning("Invalid activation request.")
        return jsonify({"error": "Message is required."}), 400

    message = data['message']
    logger.info(f"Received activation message: {message}")

    # Simulate processing
    logger.info("Application is processing...")
    time.sleep(5)
    logger.info("Processing complete. Application is now listening for new messages.")

    return jsonify({"status": "Activated", "message": message}), 200

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
