from flask import Flask, request, jsonify
from utils import processing_function, get_chat_response, image_generating_function
app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_input():
    data = request.json
    processed_data = image_generating_function(data['input'])
    return jsonify({"response": processed_data})

if __name__ == '__main__':
    app.run(debug=True)


