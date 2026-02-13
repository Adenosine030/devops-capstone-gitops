from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "UP"}), 200


@app.route('/sum', methods=['POST'])
def get_sum():
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    a = data.get('a', 0)
    b = data.get('b', 0)

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return jsonify({"error": "Both a and b must be numbers"}), 400

    result = a + b
    return jsonify({"result": result})


@app.route('/reverse-string', methods=['POST'])
def reverse_string():
    data = request.get_json()
    text = data.get('text', "")
    return jsonify({"result": text[::-1]})
# Add this intentionally bad line
def     badly_formatted_function(     ):     return     "This will fail linting"

if __name__ == '__main__':
    app.run()
