from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

students = {}

class Student(BaseModel):
    id: int
    name: str
    age: int

@app.post("/students")
def add_student(student: Student):
    students[student.id] = {
        "name": student.name,
        "age": student.age
    }
    return {
        "message": "Student added successfully",
        "student": students[student.id]
    }
