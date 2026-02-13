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
