# main.py
from fastapi import FastAPI

app = FastAPI()

@app.post("/pay")
def pay(order_id: int, amount: float):
    return {"message": f"Payment of ${amount} for order {order_id} processed"}
