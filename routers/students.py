from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.student import Student
from schemas.student import StudentCreate

router = APIRouter(prefix="/students")

@router.post("/")
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    new_student = Student(**student.dict())

    db.add(new_student)
    db.commit()

    return new_student

@router.get("/")
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()

@router.get("/{student_id}")
def get_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    return db.query(Student).filter(
        Student.id == student_id
    ).first()

@router.put("/{student_id}")
def update_student(
    student_id: int,
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    db_student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    for key, value in student.dict().items():
        setattr(db_student, key, value)

    db.commit()

    return db_student

@router.delete("/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    db.delete(student)
    db.commit()

    return {"message": "Deleted"}