from fastapi import FastAPI

app = FastAPI()

employees = {
    "Ali": 50000,
    "Ahmed": 65000,
    "Sara": 70000
}

@app.get("/employee/{name}")
def employee_salary(name: str):
    if name in employees:
        return {
            "employee": name,
            "salary": employees[name]
        }
    return {"message": "Employee not found"}
