from flask import Flask, request, jsonify

app = Flask(__name__)

prices = {
    10: 5.0,
    15: 7.5,
    20: 10.0,
    25: 12.5,
    30: 15.0
}

@app.route('/orders', methods=['POST'])
def order():
    data = request.get_json()
    msg = data['order']

    # "Order: 20L x 2"
    parts = msg.split()
    size = int(parts[1].replace('L', ''))
    qty = int(parts[-1])

    total = prices[size] * qty
    return jsonify({"size": size, "quantity": qty, "totalPrice": total})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
