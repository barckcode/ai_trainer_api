from fastapi import APIRouter, HTTPException, status, Depends, Path
from fastapi.responses import JSONResponse, Response
from sqlalchemy.orm import Session
from db.session import get_db
from utils.logs import logger
from models import ExerciseModel
from schemas import ExerciseSchema


exercises_router = APIRouter()


@exercises_router.get(
    "/exercises",
    tags=["exercises"],
    summary="Get all exercises",
    response_model=list[ExerciseSchema],
)
def get_exercises(
    db: Session = Depends(get_db)
):
    logger.info("Getting all exercises")
    exercises = db.query(ExerciseModel).all()
    if not exercises:
        logger.warning("No exercises found")
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    exercise_list = [exercise.to_dict() for exercise in exercises]
    return JSONResponse(exercise_list)
