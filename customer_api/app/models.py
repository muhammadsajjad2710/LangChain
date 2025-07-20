from sqlalchemy import Column, String, Boolean, JSON
from .database import Base

class DNISTable(Base):
    __tablename__ = "dnis_table"

    poly_num_to_call = Column(String, primary_key=True, index=True)
    locked = Column(Boolean, default=False)
    zoom_phone_ar_number = Column(String, unique=True, index=True)
    engagementId = Column(String, nullable=True)
    details = Column(JSON, nullable=True)
