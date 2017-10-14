#!/usr/bin/env python
# -*- coding: utf-8 -*-

# irkcmd.py

"""
ローカルで IRKit をプリセットコントロールするためのスクリプト
"""

import os, sys, json
import requests

__version__ = '0.0.1'

def irkMain():
    '''
    メインルーチン
    '''
    global g_cmdData # 設定用データ

    argv = sys.argv
    argc = len(argv)
    if (argc != 2):
        print 'usage python irkcmd.py <cmd>'
        print '<cmd> cmdlist: show cmdlist'
        exit()

    cmd = str(argv[1])

    # 設定ファイルの読み込み
    scriptPath = os.path.dirname(os.path.abspath(__file__))
    g_cmdData = loadConfig(scriptPath + '/irkconfig.json')

    if (cmd == 'cmdlist'):
        showCmds()
    else:
        execCmdSend(cmd)

def showCmds():
    '''
    コマンドの一覧を表示する
    '''

    cmdData = g_cmdData
    
    print '--cmdlist--'    

    for cmd in sorted(cmdData):
        print ('{0:20}: {1:30}'.format(cmd, cmdData[cmd]['memo']))
        #print cmd + ': ' + cmdData[cmd]['memo']

def execCmdSend(cmd):
    '''
    IRKit にデータを送信する
    '''
    
    cmdData = g_cmdData

    # 設定項目の存在を確認する
    if(cmd in cmdData):

        target = cmdData[cmd]['target']
        headers = {'X-Requested-With': 'curl'}
        format = cmdData[cmd]['format']
        freq = cmdData[cmd]['freq']
        data = cmdData[cmd]['data']
        message = {'format': format, 'freq': freq, 'data': data}
        reqUrl = 'http://' + target + '/messages'
        
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
        jsonData = json.load(f)
        #print json.dumps(jsonData, sort_keys = True, indent = 4)
        f.close()
        return jsonData
    else:
        return False

if __name__ == '__main__':
    irkMain()