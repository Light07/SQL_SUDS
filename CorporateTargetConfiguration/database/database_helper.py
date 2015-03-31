from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_

from database.StudyTargetCorporate import StudyTargetCorporate
from database.Corporate import Corporate
import settings
from settings import Environment,ENVIRONMENT

if Environment == ENVIRONMENT.LIVE:
    t = (settings.DATABASE["User"], settings.DATABASE["Password"], settings.DATABASE["VS1_Server"])
    et_corporate_engine = create_engine('mssql://%s:%s@%s/ET_corporate' % t, echo=True)

def get_ie_topic_by_corporate(corporate_id):
    Session = sessionmaker(bind=et_corporate_engine)
    session = Session()
    ie_topic = session.query(StudyTargetCorporate.IndustryEnglishAutoEnrolledUnit).\
        filter(StudyTargetCorporate.IsCurrent == 1,\
               and_(StudyTargetCorporate.Corporate_id == corporate_id)).scalar()
    if ie_topic:
        return int(ie_topic)
    else:
        return None

def get_corporate_id_by_corporate_code(corporate_code):
    Session = sessionmaker(bind=et_corporate_engine)
    session = Session()
    corporate_id_list = session.query(Corporate.CorporateId).\
        filter(Corporate.CorporateCode == corporate_code).scalar()
    if corporate_id_list:
        return int(corporate_id_list)