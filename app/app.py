from flask import Flask, request, jsonify, render_template
from datetime import datetime
import json
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
    """Parse WhatsApp-style order messages"""
    pattern = r'(\d+)\s*x\s*(\d+)(?:L|litre|liter)'
    matches = re.findall(pattern, message, re.IGNORECASE)

    order_items = []
    for match in matches:
        quantity = int(match[0])
        size = f"{match[1]}L"

        if size in PRODUCT_CATALOG:
            order_items.append({
                "size": size,
                "quantity": quantity,
                "price": PRODUCT_CATALOG[size]["price"]
            })

    return order_items


@app.route("/")
def home():
    return "AquaFlow API is running 🚰"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
