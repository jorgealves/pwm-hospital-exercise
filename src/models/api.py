from pydantic import BaseModel, validator
import string, float

class PatientAPIModel(BaseModel):
    id: int
    name: str
    date_of_birth: str
    id_number: float
    insurance: str
    phone_number: str

    @validator("id")
    def patient_validation(cls,value):
        if not value:
            raise ValueError("Patient doesnt exist")

class TicketsItemAPIModel(BaseModel):
    number: int
    sector: str
    patient_id: float
    event_id: float

class EventsAPIModel(BaseModel):
    id: int
    username: str
    ticket_item_name: str

