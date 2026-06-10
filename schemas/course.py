from pydantic import BaseModel

class CourseCreate(BaseModel):
    course_name: str
    course_code: str
    instructor: str
    duration: str
    is_active: bool