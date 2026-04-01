# pydantic_demo.py

from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str = 'Rahul'
    age : Optional[int] = None
    # email : EmailStr
    cgpa : float = Field(gt=0, lt=10, default=5, description='A decimal value representing')

# new_student = {'age':'32', 'email':'abc@gmail.com'}
new_student = {'age':'32', 'cgpa':5}


student = Student(**new_student)

print(type(student))
print(student)

student_dict = dict(student)

print(student_dict['age'])

student_json = student.model_dump_json()