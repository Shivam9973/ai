#postman
import requests

shipment_id = 'SH123'
response = requests.get(f'http://localhost:5000/shipment/{shipment_id}')

if response.status_code == 200:
    shipment_info = response.json()
    print(f'Shipment {shipment_id} is {shipment_info["status"]} and will be delivered to {shipment_info["destination"]} on {shipment_info["estimated_delivery_date"]}.')
else:
    print(f'Error retrieving shipment {shipment_id}.')
