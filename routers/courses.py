from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.course import Course
from schemas.course import CourseCreate

router = APIRouter(prefix="/courses")

@router.post("/")
def create_course(
    course: CourseCreate,
    db: Session = Depends(get_db)
):
    new_course = Course(**course.dict())

    db.add(new_course)
    db.commit()

    return new_course

@router.get("/")
def get_courses(db: Session = Depends(get_db)):
    return db.query(Course).all()

@router.get("/{course_id}")
def get_course(
    course_id: int,
    db: Session = Depends(get_db)
):
    return db.query(Course).filter(
        Course.id == course_id
    ).first()

@router.put("/{course_id}")
def update_course(
    course_id: int,
    course: CourseCreate,
    db: Session = Depends(get_db)
):
    db_course = db.query(Course).filter(
        Course.id == course_id
    ).first()

    for key, value in course.dict().items():
        setattr(db_course, key, value)

    db.commit()

    return db_course

@router.delete("/{course_id}")
def delete_course(
    course_id: int,
    db: Session = Depends(get_db)
):
    course = db.query(Course).filter(
        Course.id == course_id
    ).first()

    db.delete(course)
    db.commit()

    return {"message": "Deleted"}