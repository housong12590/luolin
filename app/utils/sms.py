import hmac
import json
import requests
from hashlib import sha1
from flask import current_app, jsonify
from app.notify import send_msg


def _sign_hamcsha1(key, params):
    params = {k: params[k] for k in sorted(params.keys())}
    value = ''.join('%s=%s&' % (key, value) for key, value in params.items())[:-1]
    sign = hmac.new(key.encode('utf-8'), value.encode('utf-8'), sha1)
    params['signature'] = sign.hexdigest()
    params = {k: params[k] for k in sorted(params.keys())}
    return params


def _sms_service(endpoint, data=None, method='POST'):
    if data is None:
        data = {}
    url = current_app.config['SMS_URL'] + endpoint
    params = _sign_hamcsha1(current_app.config['SMS_KEY'], data)
    if method.upper() == 'POST':
        result = requests.post(url, json.dumps(params))
    else:
        result = requests.get(url, json.dumps(params))
    if result.status_code == 200:
        return json.loads(result.text)
    else:
        send_msg('【tcmipr 短信服务】 %s  %s  %s  %s' % (method, result.url, result.status_code, params))
        return json.dumps({'status_code': 400, 'msg': '短信服务响应失败', 'data': []})


def verify_sms_code(mobile, verify_code):
    data = {
        'mobile': mobile,
        'template': 'app',
        'verification_code': verify_code
    }
    endpoint = 'verify_code'
    return _sms_service(endpoint, data)


def verify_result(mobile, verify_code):
    content = verify_sms_code(mobile, verify_code)
    print(content)
    return content['status_code'] == 200


def send_sms_code(mobile):
    data = {
        'mobile': mobile,
        'template': 'app',
    }
    return _sms_service('code', data)
