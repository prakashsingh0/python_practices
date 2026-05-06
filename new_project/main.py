from fastapi import FastAPI
from pydantic import BaseModel

studentss = []
class Students(BaseModel):
    full_name:str
    age:int
    course:str

app = FastAPI()


@app.post("/students")
async def students(student:Students):
    studentss.append(student)
    return studentss

@app.get("/find/{course}")
async def find_student_by_course(course:str):
    student = [student for student in studentss if student.course.lower() == course.lower()]
    return student

@app.get("/")
async def root():
    name = "praksh singh"
    course = "python"
    return {"name":name,"course":course}

@app.get("/items/{item_id}")
async def find_items(item_id:int):
    return {"item_id":item_id}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    try:
        if skip >1 :
            raise ValueError({"message":"please enter skip less then or equal to 1"})
        return fake_items_db[skip : skip + limit]
    except Exception as e:
        return f"some thing went wrong {e}"