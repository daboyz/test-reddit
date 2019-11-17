#!/usr/bin/env python3
from pprint import pprint

DEBUG = True

def LOG_INFO(bot_name, msg):
    '''Output info level log'''
    print('\nINFO: ' + bot_name + '  -- ' + msg)


def LOG_ERROR(error_code, msg):
    '''Output error level log'''
    error_msg = '\n!ERROR: ' + 'error code: %s' % error_code
    if msg != '':
        error_msg = error_msg + 'msg: ' + msg
    print('~'*80)
    print(error_msg + '!')
    print('~' * 80)


def LOG_DEBUG(msg):
    '''Output debug level log'''
    if not DEBUG:                   # Changed for readability
        return False
    print('\nDEBUG: ' + msg)


def LONG_DEBUG(bot_name, long_message):
    '''Output long debug level log'''
    if not DEBUG:                   # Changed for readability
        return False
    print('\nLONG_DEBUG from: ' + bot_name)
    pprint(long_message)
    print('')  # just to add free line delimiter
