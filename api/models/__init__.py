from db.config import Base, engine

# Models
from .exercises import ExerciseModel

Base.metadata.create_all(engine)
