'''
    Module that gives a logger instance
'''
import logging
import sys
from json import dumps
from datetime import datetime

def data_log(subs_list, alreary_subs_list, invalid_subs_list, subs_count, already_subs_count, invalid_subs_count):
    return dumps({
        "Subscribers": {
            "emails": subs_list,
            "count": subs_count
        },
        "AlreadySubscribed": {
            "emails": alreary_subs_list,
            "count": already_subs_count
        },
        "InvalidEmails": {
            "emails": invalid_subs_list,
            "count": invalid_subs_count
        }
    })

def _build():
    ''' Creates a logger instance '''
    log = logging.getLogger(__name__)
    out_hdlr = logging.StreamHandler(sys.stdout)
    out_hdlr.setFormatter(
        logging.Formatter('%(asctime)s [%(levelname)-5.5s] [%(funcName)s] %(message)s')
    )
    out_hdlr.setLevel(logging.INFO)
    log.addHandler(out_hdlr)
    log.setLevel(logging.INFO)
    return log

class Logger(logging.getLoggerClass()):
    ''' Singleton for log management '''
    instance = None
    def __new__(cls):
        if not Logger.instance:
            Logger.instance = _build()
        return Logger.instance
