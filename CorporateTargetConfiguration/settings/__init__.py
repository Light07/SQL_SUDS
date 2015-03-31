__author__ = 'kevin.cai'

class ENVIRONMENT(object):
    UAT = "cllsuat"
    LIVE = "cllsuat"

Environment = ENVIRONMENT.LIVE

if Environment == ENVIRONMENT.LIVE:
       DATABASE = {
          "VS1_Server": "10.128.34.249",
          "VS3_Server": "10.43.45.160",
          "User": "etownreader",
          "Password": "fishing22"
          }

wsdl_address = 'http://%s.englishtown.com/services/wcf/campuscore/StudyTargetService.svc?WSDL' %Environment

class StudyTargetService:
    WSDL = {
            'url':wsdl_address
            }

WSDL_ADDRESS = "http://cllsuat.englishtown.com/wheeljack/target.wsdl"

# WSDL_ADDRESS = StudyTargetService.WSDL['url']

