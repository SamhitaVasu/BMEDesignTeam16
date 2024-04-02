from flask import Flask, request, jsonify
from utils import processing_function, get_chat_response, image_generating_function_quantity, show_image, image_generating_function_object, image_generating_function_action, identify_parts
app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_input():
    data = request.json
    processed_data = image_generating_function_object(data['input'])
    return jsonify({"response": processed_data})

if __name__ == '__main__':
    app.run(debug=True)


