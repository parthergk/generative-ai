from pydantic import BaseModel
from typing import List, Dict, Optional

class Cart(BaseModel):
    user_if: int
    item: List[str]
    quantites: Dict[str, int]
    image: Optional[str] = None

cart_data = {
    "user_if": 123,
    "item": ["Laptop", "Mouse", "Keyboard"],
    "quantites": {"Laptop": 1, "mouse": 2, "keyboard": 3},
    # "image": "url"
}

cart = Cart(**cart_data)

print(cart)