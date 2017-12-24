#!/usr/bin/env python
# -*- coding: utf-8 -*-

# irkcmd.py

"""
IR Kit CLI Script (local network only)
"""

import os
import sys
import json
import requests

g_cmd_data = {}

__version__ = '0.0.4.171224'

def irkMain():
    '''
    Main routine
    '''
    global g_cmd_data # config global value

    argv = sys.argv
    argc = len(argv)
    if (argc != 2):
        print 'usage python irkcmd.py <cmd>'
        print '<cmd> cmdlist: show cmdlist'
        exit()

    cmd = str(argv[1])

    # loading config
    script_path = os.path.dirname(os.path.abspath(__file__))
    g_cmd_data = loadConfig(os.path.join(script_path, 'irkconfig.json'))

    if (g_cmd_data == ''):
        print 'config data is empty, please check config file'
        return False

    if (cmd == 'cmdlist'):
        showCmds()
    else:
        execCmdSend(cmd)

    return True

def showCmds():
    '''
    list commands
    '''
    cmd_data = g_cmd_data

    print '--cmdlist--'

    for cmd in sorted(cmd_data):
        print ('{0:20}: {1:30}'.format(cmd, cmd_data[cmd]['memo']))
        #print cmd + ': ' + cmdData[cmd]['memo']

def execCmdSend(cmd):
    '''
    send to IRKit
    '''
    cmd_data = g_cmd_data

    # check cmd_data
    if (cmd in cmd_data):

        target = cmd_data[cmd]['target']
        headers = {'X-Requested-With': 'curl'}
        send_format = cmd_data[cmd]['format']
        freq = cmd_data[cmd]['freq']
        data = cmd_data[cmd]['data']
        message = {'format': send_format, 'freq': freq, 'data': data}
        req_url = 'http://%s/messages' % (target)

        # send request
        r = requests.post(req_url, headers=headers, data=json.dumps(message))
        print r.status_code

    # when cmd_data is empty
    else:
        print 'cmd not found'
        print 'type: python irkcmd.py cmdlist'

def loadConfig(config_file):
    '''
    load config form config_file
    '''
    if (os.path.exists(config_file)):
        f = open(config_file, 'r')
        json_data = json.load(f)
        #print json.dumps(json_data, sort_keys = True, indent = 4)
        f.close()
        return json_data
    else:
        print 'can not read %s' % config_file

    return ''

if __name__ == '__main__':
    irkMain()
