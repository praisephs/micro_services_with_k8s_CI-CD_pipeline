# main.py
import requests
from fastapi import FastAPI

app = FastAPI()

@app.post("/create_order")
def create_order(order_id: int, product_name: str):

    # Call the Payments Service API
    payment_response = requests.post("http://payments_service:8002/pay", json={"order_id": order_id, "amount": 100.0})
    return {
        
        "message": f"Order {order_id} created for {product_name}",
        "payment_status": payment_response.json()

    }
    #return {"message": f"Order {order_id} created for {product_name}"}
