from flask import Flask , jsonify, request

app = Flask(__name__)

menu = {"Poha": 30, "Tea": 15, "Sandwich": 50}

@app.route("/menu")
def get_menu():
    return jsonify(menu)

@app.route("/order", methods = ["POST"])
def place_order():
    order = request.get_json()
    item = order["item"]
    qty = order["quantity"]
    total = menu[item]*qty
    return jsonify({
        "order.id": 101,
        "total": total,
        "status": "Order placed"
    })
app.run(port=5000)
