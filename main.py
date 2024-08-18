from fastapi import FastAPI

app = FastAPI()

@app.get("/get_items/{cuisine}")
async def get_items(cuisine):
    return f"welcome  {cuisine}"