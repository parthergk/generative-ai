from typing import Optional
from pydantic import BaseModel, Field
import re

class Employee(BaseModel):
    id: int
    name: str = Field(
        ..., 
        min_length= 3,
        max_length= 15,
        description= "Employee name",
    )
    department: Optional[str] = None

class User(BaseModel):
    email: str = Field(...,pattern=r'')
    phone: str = Field(...,pattern=r'')


emp = Employee(id=12, name="gaurav")
print(emp)