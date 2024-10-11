from flask import Flask, request, jsonify
app = Flask(__name__)

# In-memory data storage for simplicity
items = {}

# CRUD operations

# Create
@app.route('/item', methods=['POST'])
def create_item():
    data = request.get_json()
    item_id = str(len(items) + 1)
    items[item_id] = data
    return jsonify({"id": item_id, "item": data}), 201

# Read
@app.route('/item/<item_id>', methods=['GET'])
def read_item(item_id):
    item = items.get(item_id)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify({"id": item_id, "item": item})

# Update
@app.route('/item/<item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    if item_id not in items:
        return jsonify({"error": "Item not found"}), 404
    items[item_id] = data
    return jsonify({"id": item_id, "item": data})

# Delete
@app.route('/item/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id not in items:
        return jsonify({"error": "Item not found"}), 404
    del items[item_id]
    return jsonify({"message": "Item deleted"}), 200

if __name__ == '__main__':
    # HTTP
    app.run(debug=True, port=5000)
    # HTTPS
    # app.run(debug=True, port=5000, ssl_context=('certificate.pem', 'key.pem'))