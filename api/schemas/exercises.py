from pydantic import BaseModel, Field


class ExerciseSchema(BaseModel):
    id: int | None = None
    name: str = Field(..., description="The name of the exercise")
    image_url: str = Field(..., description="The image URL of the exercise")
    video_url: str = Field(..., description="The video URL of the exercise")
