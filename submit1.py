# -*- coding: utf-8 -*-

import requests
from shibboleth_login import ShibbolethClient

ID = input('your username: ')
PW = input('your passsword: ')

with ShibbolethClient(ID, PW) as client:
    res = client.get('https://portal.student.kit.ac.jp/')

print(res.text)
# f = open('submit1.html', 'w') # 書き込みモードで開く
# f.write(res.text) # 引数の文字列をファイルに書き込む
# f.close() # ファイルを閉じる
client.close()
