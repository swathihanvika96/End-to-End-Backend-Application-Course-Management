from fastapi import FastAPI

from database import Base, engine

from routers import (
    auth,
    students,
    courses,
    enrollments
)

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(students.router)
app.include_router(courses.router)
app.include_router(enrollments.router)