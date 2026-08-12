from sqlalchemy import Column, Integer, String
from app.db.database import Base


class Facility(Base):
    __tablename__ = "facilities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    facility_type = Column(String, nullable=False)
    city = Column(String, nullable=False)
    address = Column(String, nullable=True)