from fastapi import FastAPI

app = FastAPI(root_path="/")

@app.get("/")
async def root() -> str:
    return "Welcome to the Authentication Validator Engine"

