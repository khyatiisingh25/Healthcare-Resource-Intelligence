from pydantic import BaseModel


class FacilityCreate(BaseModel):
    name: str
    facility_type: str
    city: str
    address: str | None = None


class FacilityResponse(BaseModel):
    id: int
    name: str
    facility_type: str
    city: str
    address: str | None = None

    class Config:
        from_attributes = True