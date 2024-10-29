from sqlalchemy import Column, String, Integer, Float, ForeignKey
#from sqlalchemy.orm import relationship
from db.config import Base


class ExerciseModel(Base):
    __tablename__ = 'exercises'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    image_url = Column(String, nullable=False)
    video_url = Column(String, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "image_url": self.image_url,
            "video_url": self.video_url,
        }
