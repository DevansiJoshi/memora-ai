from fastapi import FastAPI

app = FastAPI(
    title="Memora AI",
    version="1.0.0",
    description="AI Powered Knowledge Operating System"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Memora AI 🚀"
    }