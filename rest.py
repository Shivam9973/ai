from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/shipment/<shipment_id>')
def get_shipment(shipment_id):
    shipment_info = {
        "id": shipment_id,
        "status": "in transit",
        "destination": "New York",
        "estimated_delivery_date": "2023-04-15"
    }
    return jsonify(shipment_info)

if __name__ == '__main__':
    app.run()
