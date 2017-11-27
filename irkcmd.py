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

__version__ = '0.0.2.171127'

def irkMain():
    '''
    メインルーチン
    '''
    global g_cmd_data # 設定用データ

    argv = sys.argv
    argc = len(argv)
    if (argc != 2):
        print 'usage python irkcmd.py <cmd>'
        print '<cmd> cmdlist: show cmdlist'
        exit()

    cmd = str(argv[1])

    # 設定ファイルの読み込み
    script_path = os.path.dirname(os.path.abspath(__file__))
    g_cmd_data = loadConfig(os.path.join(script_path, 'irkconfig.json'))

    if (cmd == 'cmdlist'):
        showCmds()
    else:
        execCmdSend(cmd)

def showCmds():
    '''
    コマンドの一覧を表示する
    '''

    cmd_data = g_cmd_data

    print '--cmdlist--'

    for cmd in sorted(cmd_data):
        print ('{0:20}: {1:30}'.format(cmd, cmd_data[cmd]['memo']))
        #print cmd + ': ' + cmdData[cmd]['memo']

def execCmdSend(cmd):
    '''
    IRKit にデータを送信する
    '''
    cmd_data = g_cmd_data

    # 設定項目の存在を確認する
    if(cmd in cmd_data):

        target = cmd_data[cmd]['target']
        headers = {'X-Requested-With': 'curl'}
        send_format = cmd_data[cmd]['format']
        freq = cmd_data[cmd]['freq']
        data = cmd_data[cmd]['data']
        message = {'format': send_format, 'freq': freq, 'data': data}
        reqUrl = 'http://%s/messages' % (target)

        # リクエストの送信
        r = requests.post(reqUrl, headers=headers, data=json.dumps(message))
        print r.status_code

    # 設定項目がない場合
    else:
        print 'cmd not found'
        print 'type: python irkcmd.py cmdlist'

def loadConfig(configFile):
    '''
    設定ファイルを読み出す
    '''
    if (os.path.exists(configFile)):
        f = open(configFile, 'r')
        json_data = json.load(f)
        #print json.dumps(json_data, sort_keys = True, indent = 4)
        f.close()
        return json_data
    return False

if __name__ == '__main__':
    irkMain()
