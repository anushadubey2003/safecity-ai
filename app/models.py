from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Crime(Base):
    __tablename__ = 'crimes'
    id = Column(Integer, primary_key=True)
    district = Column(String)
    crime_type = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    date = Column(String)
