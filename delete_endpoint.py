from fastapi import FastAPI

app = FastAPI()

students = {
    1: {"name": "Ali", "age": 20},
    2: {"name": "Sara", "age": 21}
}

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"message": "Student not found"}

    deleted_student = students.pop(student_id)

    return {
        "message": "Student deleted successfully",
        "student": deleted_student
    }
