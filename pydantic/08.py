from pydantic import BaseModel, field_validator

class Name(BaseModel):
    first_name: str
    last_name: str

    @field_validator("first_name", "last_name")
    def name_validate(cls, v):
        if not v.istitle():
            raise ValueError("Names must be capitilized")
        return v
    
name = Name(first_name="Gaurav", last_name="Kumar")
print(name.name_validate)