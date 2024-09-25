# main.py

# from fastapi import FastAPI, Form
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# from starlette.requests import Request

# app = FastAPI()

# # Load templates from the 'templates' folder
# templates = Jinja2Templates(directory="templates")

# # Display the login page
# @app.get("/login", response_class=HTMLResponse)
# async def get_login_page(request: Request):
#     return templates.TemplateResponse("login.html", {"request": request})

# # Handle the form submission
# @app.post("/login")
# async def login(username: str = Form(...), password: str = Form(...)):
#     # For demonstration purposes, we're not validating the password.
#     return {"message": f"User {username} logged in"}

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.status import HTTP_302_FOUND

app = FastAPI()

# Load templates from the 'templates' folder
templates = Jinja2Templates(directory="templates")

# Display the login page
@app.get("/login", response_class=HTMLResponse)
async def get_login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# Handle the login form submission
@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    # For now, just simulate a successful login (no actual authentication)
    if username == "admin" and password == "password":  # Simplified login check
        return RedirectResponse(url="/dashboard", status_code=HTTP_302_FOUND)
    return {"message": "Invalid credentials, please try again."}

# Display the dashboard with buttons for the orders_service
@app.get("/dashboard", response_class=HTMLResponse)
async def get_dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

