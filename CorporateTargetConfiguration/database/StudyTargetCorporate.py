__author__ = 'kevin.cai'

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()
class StudyTargetCorporate(Base):
    __tablename__ = 'StudyTargetCorporate'
    CorporateTarget_id = Column(Integer, primary_key=True)
    Corporate_id = Column(Integer)
    GeneralEnglishTarget = Column(Integer)
    BusinessEnglishTarget = Column(Integer)
    IndustryEnglishTarget = Column(Integer)
    IndustryEnglishAutoEnrolledUnit = Column(Integer)
    ActiveFrom = Column(DateTime)
    ActiveTo = Column(DateTime)
    IsCurrent = Column(Integer)