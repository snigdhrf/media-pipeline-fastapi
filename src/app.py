from fastapi import FastAPI, HTTPException

app = FastAPI()

text_posts = {
  "1": {"title": "New Post", "content": "This is my first post!"},
  "2": {"title": "Morning Thoughts", "content": "Coffee tastes better on Mondays."},
  "3": {"title": "Tech Update", "content": "Exploring new AI tools today."},
  "4": {"title": "Travel Plans", "content": "Thinking about a trip to the mountains."},
  "5": {"title": "Workout Log", "content": "Completed a 5km run today."},
  "6": {"title": "Book Notes", "content": "Reading a fascinating sci-fi novel."},
  "7": {"title": "Recipe Idea", "content": "Trying out homemade pasta tonight."},
  "8": {"title": "Daily Reflection", "content": "Grateful for small wins today."},
  "9": {"title": "Learning Log", "content": "Practiced Python data structures."},
  "10": {"title": "Weekend Plans", "content": "Catching up with friends and relaxing."}
}

@app.get("/posts")
def get_all_posts(limit : int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

#path parameter
@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code = 404, detail = "Post not found")
    
    return text_posts.get(id)

