from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Welcome to Coffee Shop API",
        "docs": "/docs",
        "version": "1.0.0"
    }