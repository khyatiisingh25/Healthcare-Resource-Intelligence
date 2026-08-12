from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.models.facility import Facility
from app.schemas.facility import FacilityCreate, FacilityResponse


router = APIRouter(
    prefix="/facilities",
    tags=["Facilities"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=FacilityResponse)
def create_facility(
    facility: FacilityCreate,
    db: Session = Depends(get_db)
):
    new_facility = Facility(
        name=facility.name,
        facility_type=facility.facility_type,
        city=facility.city,
        address=facility.address
    )

    db.add(new_facility)
    db.commit()
    db.refresh(new_facility)

    return new_facility