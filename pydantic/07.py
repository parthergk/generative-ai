from pydantic import BaseModel, computed_field

class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int
    rate_per_night: float

    @computed_field
    @property
    def total_amount(self) -> float:
        return self.nights * self.rate_per_night
    
booking = Booking(user_id=123, room_id= 47, nights=4, rate_per_night=100.5)

print(booking.total_amount)