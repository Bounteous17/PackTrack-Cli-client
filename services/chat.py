import requests
from utils import functions as _functions, defaults as _defaults
from services import utils as _sUtils

def innit(username):
    try:
        r = _sUtils.request('/chat', {'username': username}, _defaults.access_token).post()
        r.res.raise_for_status()
        return r
    except requests.exceptions.HTTPError as err:
        return _functions.setModuleError(payload=err, error=r.body['msg'])

def list():
    try:
        r = _sUtils.request('/chat', {}, _defaults.access_token).get()
        r.res.raise_for_status()
        return r
    except requests.exceptions.HTTPError as err:
        return _functions.setModuleError(payload=err, error=r.body['msg'])
