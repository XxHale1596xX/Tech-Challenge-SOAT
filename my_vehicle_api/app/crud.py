from sqlalchemy.orm import Session
from app import models, schemas
from fastapi import HTTPException

def create_vehicle(db: Session, vehicle: schemas.VehicleCreate):
    db_vehicle = models.Vehicle(**vehicle.dict())
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle

def update_vehicle(db: Session, vehicle_id: int, vehicle: schemas.VehicleUpdate):
    db_vehicle = db.query(models.Vehicle).filter(models.Vehicle.id == vehicle_id).first()
    if not db_vehicle:
        return None  # Retorna None se o veículo não for encontrado
    
    for var, value in vars(vehicle).items():
        setattr(db_vehicle, var, value) if value is not None else None
    
    db.commit()
    db.refresh(db_vehicle)  # Refresh para obter os dados mais atuais
    return db_vehicle

def sell_vehicle(db: Session, vehicle_id: int, sale: schemas.SaleCreate):
    # Verifique se o veículo existe
    vehicle = db.query(models.Vehicle).filter(models.Vehicle.id == vehicle_id).first()
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")

    # Verifique se o veículo já foi vendido
    if vehicle.is_sold:
        raise HTTPException(status_code=400, detail="Vehicle already sold")

    # Criar uma nova venda
    db_sale = models.Sale(
        vehicle_id=vehicle.id,
        customer_cpf=sale.customer_cpf,
        sale_date=sale.sale_date  # Espera-se que esta data seja fornecida no schema de entrada
    )
    
    vehicle.is_sold = True  # Atualizando o estado do veículo
    
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)  # Recupera os dados atualizados da venda
    
    return db_sale  # Certifique-se de retornar o objeto de venda criado

def get_vehicles_sold(db: Session):
    """
    Retorna uma lista de veículos que foram vendidos, ordenados por preço do mais barato ao mais caro.
    """
    return db.query(models.Vehicle).filter(models.Vehicle.is_sold == True).order_by(models.Vehicle.price).all()