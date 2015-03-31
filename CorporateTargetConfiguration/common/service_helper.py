import settings

from suds.client import Client
from suds.wsse import *

from settings import StudyTargetService

def set_corporate_study_target(corporate_id, ge_target, be_target, ie_target, ie_topic, apply_to_all):
    serviceWSDL = settings.WSDL_ADDRESS
    studyTargetClient = call_service(serviceWSDL)
    targetInfo = studyTargetClient.factory.create('SaveCorporateStudyTarget')
    targetInfo.param.CorporateId = corporate_id
    targetInfo.param.GeneralEnglishTarget = ge_target
    targetInfo.param.BusinessEnglishTarget = be_target
    targetInfo.param.IndustryEnglishTarget = ie_target
    targetInfo.param.IndustryEnglishAutoEnrolledUnit = ie_topic
    targetInfo.param.ApplyToAllSubscriptions = apply_to_all
    response = studyTargetClient.service.SaveCorporateStudyTarget(targetInfo.param)

def get_corporate_study_target(member_id, subscription_id):
    service_wsdl = settings.WSDL_ADDRESS
    study_target_client = call_service(service_wsdl)
    target = study_target_client.factory.create('LoadCalculatedStudyTarget')
    target.memberId = member_id
    target.subscriptionId = subscription_id
    response = study_target_client.service.LoadCalculatedStudyTarget(target.memberId, target.subscriptionId)
    return response

def call_service(serviceWSDL, securityUser = None):
    client = Client(serviceWSDL)
    if securityUser:           
        security = Security()
        token = UsernameToken(securityUser.get('userName'), securityUser.get('password'))
        security.tokens.append(token)
        client.set_options(wsse = security)
    return client


