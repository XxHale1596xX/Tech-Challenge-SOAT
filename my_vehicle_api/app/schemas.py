from pydantic import BaseModel
from datetime import date

class VehicleBase(BaseModel):
    brand: str
    model: str
    year: int
    color: str
    price: float

class VehicleCreate(VehicleBase):
    pass

class VehicleUpdate(VehicleBase):
    pass

class Vehicle(VehicleBase):
    id: int
    is_sold: bool

    class Config:
        orm_mode = True

class SaleCreate(BaseModel):
    customer_cpf: str
    sale_date: date

class Sale(BaseModel):
    id: int
    vehicle_id: int
    customer_cpf: str
    sale_date: date

    class Config:
        orm_mode = True

class PaymentNotification(BaseModel):
    payment_code: str
    status: str