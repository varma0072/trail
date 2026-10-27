
from fastapi import FastAPI

app = FastAPI(title="Job Tracker API")


@app.get("/")
def home():
    return {"message": "Welcome to my FastAPI application"}


@app.get("/jobs")
def get_jobs():
    return [
        {
            "id": 1,
            "company": "Amazon",
            "role": "Java Backend Developer"
        },
        {
            "id": 2,
            "company": "Microsoft",
            "role": "Python Developer"
        }
    ]
