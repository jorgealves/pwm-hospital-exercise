from src.models.database import PatientDatabaseModel, EventsDatabaseModel
from src.models.api import PatientAPIModel, EventItemAPIModel
from src.models.database import MenuItemDatabaseModel, engine, OrderDatabaseModel
from dataclasses import asdict
from sqlalchemy.orm import Session
from sqlalchemy import select, delete
from passlib.context import CryptContext


def create_new_patient(Patient_api_model: PatientAPIModel):
    with Session(engine) as session:
        new_patient = PatientDatabaseModel(**Patient_api_model.dict())
        session.add(new_patient)
        session.commit()


def get_id_number(id_number: float) -> PatientDatabaseModel:
    with Session(engine) as session:
        query = select(PatientDatabaseModel).where(
            PatientDatabaseModel.id_mumber == id_number)
        result = session.scalars(query).one()
    if not result:
        raise Exception("id_number does not exist")
    return result


def create_event(event_api_model: EventItemAPIModel):
    with Session(engine) as db:
        new_event = EventsDatabaseModel(**event_api_model.dict())
        db.add(new_event)
        db.commit()


def get_all_patients():
    with Session(engine) as db:
        query = select(PatientDatabaseModel)
        result = db.scalars(query).all()
    return list(result)
