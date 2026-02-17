from pydantic import BaseModel, field_validator, model_validator

class User(BaseModel):
    username: str

    @field_validator('username')
    def username_validator(cls, v):
        if len(v) < 4:
            raise ValueError("Username must be at least 4 characters")
        return v
    

usr = User(username = "roni")
print(usr.username)

class SignupData(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def passw(cls, val):
        if val.password != val.confirm_password:
            raise ValueError("password do not match")
        return val