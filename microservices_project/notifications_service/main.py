# main.py
from fastapi import FastAPI

app = FastAPI()

@app.post("/notify")
def notify(order_id: int, message: str):
    return {"message": f"Notification sent for order {order_id}: {message}"}
