from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
import httpx
from typing import Optional
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI()
HACKERNEWS_API_URL = os.getenv("HACKERNEWS_API_URL")
STORY_URL = os.getenv("STORY_URL")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
)


class Story(BaseModel):
    title: str
    author: str
    url: Optional[str]
    score: int
    time: str

@app.get("/top-stories", response_model=list[Story])
async def get_top_stories():
    async with httpx.AsyncClient() as client:
        # Fetch the top 10 story IDs
        response = await client.get(HACKERNEWS_API_URL)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="HackerNews API is down")
        story_ids = response.json()[:10]

        stories = []
        for story_id in story_ids:
            story_response = await client.get(STORY_URL.format(id=story_id))
            if story_response.status_code != 200:
                raise HTTPException(status_code=story_response.status_code, detail="HackerNews API is down")
            data = story_response.json()
            stories.append({
                "title": data.get("title"),
                "author": data.get("by"),
                "url": data.get("url"),
                "score": data.get("score"),
                "time": datetime.fromtimestamp(data.get("time")).strftime("%Y-%m-%d %H:%M:%S")
            })
        return stories
