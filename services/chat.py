import requests
from utils import functions as _functions, defaults as _defaults
from services import utils as _sUtils

def innit(username):
    try:
        r = _sUtils.request(endpoint='/chat', body={'username': username}, headers=_defaults.access_token).post()
        r.res.raise_for_status()
        return r
    except requests.exceptions.HTTPError as err:
        return _functions.setModuleError(payload=err, error=r.body['msg'])
