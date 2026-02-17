from pydantic import BaseModel, model_validator 

class Signature(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def password_conf(cls, values):
        if values.password != values.confirm_password:
            raise ValueError("Passord do not match")
        return values