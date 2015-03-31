__author__ = 'kevin.cai'

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, BOOLEAN

Base = declarative_base()
class Corporate(Base):
    __tablename__ = 'Corporate'

    CorporateId = Column(Integer, primary_key=True)
    CorporateCode = Column(String)
    IsActive = Column(BOOLEAN)