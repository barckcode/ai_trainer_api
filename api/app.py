import logging
from fastapi import FastAPI
from routes import exercises_router

logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title="AI Trainer API",
    description="AI Trainer API",
    version="0.0.1",
    openapi_tags=[
        {
            "name": "exercises",
            "description": "Exercises Endpoints",
        },
    ],
)

app.include_router(exercises_router)
