from fastapi import FastAPI

app = FastAPI()


song_db = ["evermore", "willow", "champagne problems", "gold rush",
           "'tis the damn season'", "tolerate it", "no body no crime",
           "happiness", "dorothea", "coney island",
           "ivy", "cowboy like me", "long story short"]


@app.get("/name/{name}")
async def get_name(name):
    return {"message": f"Hello {name}"}


@app.get("/songs/{song_id}")
async def get_song(song_id):
    return {"song_id": song_id, "song_name": song_db[song_id]}