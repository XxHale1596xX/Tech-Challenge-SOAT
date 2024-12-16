from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app import models, crud, schemas, database

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

@app.post("/vehicles/", response_model=schemas.Vehicle)
def create_vehicle(vehicle: schemas.VehicleCreate, db: Session = Depends(database.get_db)):
    return crud.create_vehicle(db=db, vehicle=vehicle)

@app.put("/vehicles/{vehicle_id}", response_model=schemas.Vehicle)
def update_vehicle(vehicle_id: int, vehicle: schemas.VehicleUpdate, db: Session = Depends(database.get_db)):
    db_vehicle = crud.update_vehicle(db=db, vehicle_id=vehicle_id, vehicle=vehicle)
    if not db_vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return db_vehicle

@app.post("/vehicles/{vehicle_id}/sell", response_model=schemas.Sale)
def sell_vehicle(vehicle_id: int, sale: schemas.SaleCreate, db: Session = Depends(database.get_db)):
    return crud.sell_vehicle(db=db, vehicle_id=vehicle_id, sale=sale)

# Listar veículos à venda
@app.get("/vehicles/for-sale/", response_model=List[schemas.Vehicle])
def list_vehicles_for_sale(db: Session = Depends(database.get_db)):
    return crud.get_vehicles_for_sale(db=db)

# Listar veículos vendidos
@app.get("/vehicles/sold/", response_model=List[schemas.Vehicle])
def list_vehicles_sold(db: Session = Depends(database.get_db)):
    return crud.get_vehicles_sold(db=db)

@app.post("/payment-webhook/")
def payment_webhook(payment: schemas.PaymentNotification):
    # Logic for handling payment notification
    return {"message": "Payment processed"}