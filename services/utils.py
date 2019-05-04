import requests
from utils import functions as _functions, defaults as _defaults

class request():
    def __init__(self, endpoint, body, authorization={}):
        self.endpoint = endpoint
        self.body = body
        self.authorization = authorization

    def post(self):
        r = requests.post(f'{_defaults.api_url}{self.endpoint}', data = self.body, headers = self.authorization)
        enc_res = _functions.encodeJson(r.text)
        return response(res=r, status=r.status_code, body=enc_res)

    def get(self):
        r = requests.get(f'{_defaults.api_url}{self.endpoint}', headers = self.authorization)
        enc_res = _functions.encodeJson(r.text)
        return response(res=r, status=r.status_code, body=enc_res)

class response():
    def __init__(self, **args):
        self.res = args.get('res')
        self.status = args.get('status')
        self.body = args.get('body')
