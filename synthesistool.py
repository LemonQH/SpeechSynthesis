import sys
import uuid
import requests
import hashlib

from imp import reload


reload(sys)

YOUDAO_URL = 'https://openapi.youdao.com/ttsapi'
APP_KEY = 'xxxx'
APP_SECRET = 'xxxxxx'


def encrypt(signStr):
    hash_algorithm = hashlib.md5()
    hash_algorithm.update(signStr.encode('utf-8'))
    return hash_algorithm.hexdigest()


def truncate(q):
    if q is None:
        return None
    size = len(q)
    return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]


def do_request(data):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return requests.post(YOUDAO_URL, data=data, headers=headers)


def connect(text,lang_type):
    q = text

    data = {}
    data['langType'] = lang_type
    salt = str(uuid.uuid1())
    signStr = APP_KEY + q + salt + APP_SECRET
    sign = encrypt(signStr)
    data['appKey'] = APP_KEY
    data['q'] = q
    data['salt'] = salt
    data['sign'] = sign

    response = do_request(data)
    return response
