from fastapi import FastAPI

app = FastAPI()

students = {
    1: {"name": "Ali", "age": 20},
    2: {"name": "Sara", "age": 21}
}

@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id in students:
        return students[student_id]
    return {"message": "Student not found"}
