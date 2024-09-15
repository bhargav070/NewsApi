# News Api Backend
- It handles requests from frontend and fetch news in json format from hackernews api.

# Installation
- clone repository
- pip install fastapi uvicorn https dotenv
- run the server using `uvicorn main:app --reload`

- .env has following urls 
    HACKERNEWS_API_URL = "https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty"
    STORY_URL = "https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty"



# News Api Frontend
- It shows top 10 news fetched from Hacker News api.
- Using axios to get data for latest(10) news at end point `http://127.0.0.1:8000/top-stories`
- Responsive design

# Installation
- Clone the repository
- Run `npm start`

# usage
- open `http://localhost:3000/`