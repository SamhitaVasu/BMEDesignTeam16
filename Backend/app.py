from flask import Flask, request, jsonify
from utils import processing_function, get_chat_response, image_generating_function_quantity, show_image, image_generating_function_object, image_generating_function_action, identify_parts
app = Flask(__name__)

@app.route("/parts", methods=["GET"])
def id_parts():
    data = request.json
    parts = identify_parts(data['input'])
    return jsonify({"response": parts})

@app.route("/actionImage", methods=["GET"])
def gen_action():
    data = request.json
    action_image = image_generating_function_action(data['input'])
    return jsonify({"response": action_image})

@app.route('/objectImage', methods=['GET'])
def gen_object():
    data = request.json
    object_image = image_generating_function_object(data['input'])
    return jsonify({"response": object_image})

@app.route('/quantImage', methods=['GET'])
def gen_quant():
    data = request.json
    quant_image = image_generating_function_quantity(data['input'])
    return jsonify({"response": quant_image})

if __name__ == '__main__':
    app.run(debug=True)


