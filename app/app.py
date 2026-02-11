from flask import Flask, request, jsonify, render_template
from datetime import datetime
import re

app = Flask(__name__)

# Product catalog
PRODUCT_CATALOG = {
    '20L': {'name': '20 Litre Water Can', 'price': 60},
    '10L': {'name': '10 Litre Water Can', 'price': 35},
    '5L': {'name': '5 Litre Water Can', 'price': 20},
    '1L': {'name': '1 Litre Bottle', 'price': 15}
}

def parse_order_message(message):
    pattern = r'(\d+)\s*x\s*(\d+)(?:L|litre|liter)'
    matches = re.findall(pattern, message, re.IGNORECASE)
    items = []

    for qty, size in matches:
        size = f"{size}L"
        if size in PRODUCT_CATALOG:
            price = PRODUCT_CATALOG[size]['price']
            items.append({
                'size': size,
                'quantity': int(qty),
                'unit_price': price,
                'total': int(qty) * price
            })
    return items

def calculate_bill(items):
    subtotal = sum(i['total'] for i in items)
    tax = round(subtotal * 0.18, 2)
    delivery = 20 if subtotal < 200 else 0
    return {
        'subtotal': subtotal,
        'tax': tax,
        'delivery_charge': delivery,
        'total': round(subtotal + tax + delivery, 2)
    }

@app.route('/')
def home():
    return "AquaFlow API is running 🚰"

@app.route('/api/health')
def health():
    return jsonify({
        'status': 'healthy',
        'service': 'AquaFlow Water Delivery',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/order', methods=['POST'])
def order():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({'error': 'No order message provided'}), 400

    items = parse_order_message(data['message'])
    if not items:
        return jsonify({'error': 'Invalid order'}), 400

    bill = calculate_bill(items)
    return jsonify({
        'items': items,
        'bill_summary': bill
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=False)
