steps for backend setup (FastApi)
- pip install fastapi uvicorn https dotenv

- .env has following urls 
    HACKERNEWS_API_URL = "https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty"
    STORY_URL = "https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty"

- run the server using `uvicorn main:app --reload`


steps for frontend (React)
- run the server using `npm start`
