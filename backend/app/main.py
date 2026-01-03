from fastapi import FastAPI

app = FastAPI(
    title="Atlas API",
    version="0.1.0",
    description="Backend API for Atlas – a developer collaboration platform",
)

@app.get("/", tags=["root"])
def message():
    return {"message": "WELCOME TO ATLAS"}

@app.get("/health", tags=["health"])
def health_check():
    return {"status": "ok"}
