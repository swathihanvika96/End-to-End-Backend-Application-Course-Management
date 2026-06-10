from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.enrollment import Enrollment
from schemas.enrollment import EnrollmentCreate

router = APIRouter(prefix="/enrollments")

@router.post("/")
def enroll(
    enrollment: EnrollmentCreate,
    db: Session = Depends(get_db)
):

    existing = db.query(Enrollment).filter(
        Enrollment.student_id == enrollment.student_id,
        Enrollment.course_id == enrollment.course_id
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Already Enrolled"
        )

    new_enrollment = Enrollment(
        **enrollment.dict()
    )

    db.add(new_enrollment)
    db.commit()

    return {"message": "Enrollment Successful"}