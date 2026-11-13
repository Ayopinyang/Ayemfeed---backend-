
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Ayemfeed Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Ayemfeed backend is live"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/api/feed")
def get_feed():
    return {
        "posts": [
            {"id": 1, "user": "Ayemfeed", "text": "Welcome to Ayemfeed!", "likes": 12},
            {"id": 2, "user": "Test User", "text": "First post on the feed", "likes": 5},
        ]
    }
