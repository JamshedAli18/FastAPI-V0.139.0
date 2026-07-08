from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {"name": "Ali", "age": 20}
}

class Student(BaseModel):
    name: str
    age: int

@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    if student_id not in students:
        return {"message": "Student not found"}

    students[student_id] = {
        "name": student.name,
        "age": student.age
    }

    return {
        "message": "Student updated successfully",
        "student": students[student_id]
    }
