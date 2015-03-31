__author__ = 'kevin.cai'

from common.service_helper import get_corporate_study_target, set_corporate_study_target
from database.database_helper import get_corporate_id_by_corporate_code,get_ie_topic_by_corporate
from source import corporate_code_list,corporate_code_list1, corporate_id_list, corporate_id_list1


if __name__=='__main__':
    target_list = corporate_id_list
    # input the GE ,BE, IE, Apply to ALL  that you want to configure
    ge_target = 6
    be_target = None
    ie_target = None
    ie_topic = None
    apply_to_all = True

    for list in target_list:
        corporate_id = list
        # corporate_id = get_corporate_id_by_corporate_code(list)
        # ie_topic = get_ie_topic_by_corporate(corporate_id)
        # set GE, BE, IE,Apply to ALL as configured, set ie_topic from their original value
        set_corporate_study_target(corporate_id, ge_target, be_target, ie_target, ie_topic, apply_to_all)

