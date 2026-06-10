from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    course_name = Column(String(50))
    course_code = Column(String(30), unique=True)
    instructor = Column(String(50))
    duration = Column(String(30))
    is_active = Column(Boolean, default=True)