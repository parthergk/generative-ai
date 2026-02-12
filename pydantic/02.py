from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True


pro = Product(id='12', name='str', price=12.4)

print(pro.name)