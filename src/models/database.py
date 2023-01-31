from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import String, Column, String, Float, Integer, ForeignKey
from sqlalchemy import create_engine
from src.config import Settings
from passlib.context import CryptContext
# Creates connector to the database
engine = create_engine(Settings().database_connection)

BaseDatabaseModel = declarative_base()

# Models Definition

class PatientDatabaseModel(BaseDatabaseModel):
    __tablename__ = "Patient"

    id = Column(Integer)
    name = Column(String(50))
    date_of_birth = Column(String(100))
    id_number = Column(Float(20), primary_key=True)
    insurance = Column(String(30))
    phone_number = Column(String(30))

    tickets = relationship("TicketsDatabaseModel")

class TicketsItemDatabaseModel(BaseDatabaseModel):
    __tablename__ = "tickets"

    number = Column(Integer, primary_key=True)
    sector = Column(String(100))
    patient_id = Column(Float)
    event_id = Column(Float)

    events = relationship("EventsDatabaseModel")
    patient = relationship("PatientDatabaseModel")

class EventsDatabaseModel(BaseDatabaseModel):
    __tablename__="events"

    id=Column(Integer, primary_key=True)
    username = Column(String(100), ForeignKey("UserDatabaseModel.username"))
    menu_item_name = Column(String(100), ForeignKey("MenuItemDatabaseModel.name"))

# create all tables in database
BaseDatabaseModel.metadata.create_all(engine)