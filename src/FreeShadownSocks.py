#!/usr/bin/python
# -*- coding: UTF-8 -*-
# --------------------------
# Author fzl
# Date 2017/7/20 15:13
# EMAIL fangjalylong@qq.com
# Desc 
# --------------------------
import json

import requests
import sys

from ExeUtil import ExeUtil

type = sys.getfilesystemencoding()

print( "***************************************************************")
print( "*                                                             *").decode('utf-8').encode(type)
print( "*******************欢迎使用免费代理更新程序********************").decode('utf-8').encode(type)
print( "*                                                             *").decode('utf-8').encode(type)
print( "*******************正在更新配置文件，请稍后********************").decode('utf-8').encode(type)
print( "*                                                             *").decode('utf-8').encode(type)
print( "***************************************************************")

url = 'http://121.42.170.72:8080/Shadowsocks/getAccount'
data = requests.get(url)
beans=json.loads(data.text)
file=open("gui-config.json","w+")
file.write('''{
  "configs": ['''+'\n')
for index in range(len(beans)):
    file.writelines('{')
    file.write('''"server": "'''+beans[index]['address'].strip()+'''"'''+',\n')
    file.write('''"server_port": "'''+beans[index]['port'].strip()+'''"'''+',\n')
    file.write('''"password": "'''+beans[index]['password'].strip()+'''"'''+',\n')
    file.write('''"method": "'''+beans[index]['method'].strip()+'''"'''+',\n')
    file.write('''"remarks": "'''+beans[index]['address'].strip()+'''"'''+',\n')
    file.write('''"timeout": "'''+'5'+'''"'''+'\n')
    if index==len(beans)-1:
        file.writelines('}')
    else:
        file.writelines('},')



file.write(''' ],
  "strategy": null,
  "index": 0,
  "global": true,
  "enabled": false,
  "shareOverLan": true,
  "isDefault": false,
  "localPort": 1080,
  "pacUrl": null,
  "useOnlinePac": false,
  "secureLocalPac": true,
  "availabilityStatistics": false,
  "autoCheckUpdate": true,
  "checkPreRelease": false,
  "isVerboseLogging": true,
  "logViewer": {
    "topMost": false,
    "wrapText": true,
    "toolbarShown": false,
    "Font": "Consolas, 8pt",
    "BackgroundColor": "Black",
    "TextColor": "White"
  },
  "proxy": {
    "useProxy": false,
    "proxyType": 0,
    "proxyServer": "",
    "proxyPort": 0,
    "proxyTimeout": 3
  },
  "hotkey": {
    "SwitchSystemProxy": "",
    "SwitchSystemProxyMode": "",
    "SwitchAllowLan": "",
    "ShowLogs": "",
    "ServerMoveUp": "",
    "ServerMoveDown": ""
  }
}''')
file.close()
print( "*                                                             *").decode('utf-8').encode(type)
print( "*    SS默认选中第一个代理账号，如不可用请尝试切换其他账号     *").decode('utf-8').encode(type)
print( "*                                                             *").decode('utf-8').encode(type)
print( "*                                                             *").decode('utf-8').encode(type)
print( "*             配置文件已经更新,Shadowsocks已经启动            *").decode('utf-8').encode(type)
print( "*                                                             *").decode('utf-8').encode(type)
print( "*                                                             *").decode('utf-8').encode(type)
print( "*                                               by：flyou     *").decode('utf-8').encode(type)
print( "*                                                             *").decode('utf-8').encode(type)
print( "*                                    http://www.flyou.ren     *").decode('utf-8').encode(type)
print( "*                                                             *").decode('utf-8').encode(type)
print( "***************************************************************")
exeUtil=ExeUtil('.','Shadowsocks.exe')
exeUtil.openExe()

