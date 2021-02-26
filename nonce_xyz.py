# -- coding: utf-8 --
# @Time : 2021/2/26 14:21
# @Author : Los Angeles Clippers

import execjs


def get_nonce_xyz():
    with open('nonce_xyz.js', 'r') as f:
        js = f.read()
        f.close()
    com = execjs.compile(js)
    nonce = com.call('j')
    xyz = com.call('b')

    print('nonce:', nonce)
    print('xyz:', xyz)

get_nonce_xyz()





import hashlib

a = "/xdnphb/data/weixinuser/searchWeixinDataByCondition?AppKey=joker&filter=&hasDeal=false&keyName=gzyxgzyxw&order=relation&nonce="
xyz = hashlib.md5(a.encode(encoding='UTF-8')).hexdigest()
print('xyz:', xyz)