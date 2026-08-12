from pydantic import BaseModel


class FacilityCreate(BaseModel):
    name: str
    facility_type: str
    city: str
    latitude: float
    longitude: float


class FacilityResponse(BaseModel):
    id: int
    name: str
    facility_type: str
    city: str
    latitude: float
    longitude: float

    class Config:
        from_attributes = True