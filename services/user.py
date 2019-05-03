import requests
from utils import functions as _functions, defaults as _defaults
from services import utils as _sUtils

def signup(user):
    try:
        r = _sUtils.request('/signup', {'username': user.username, 'password': user.password}).post()
        r.res.raise_for_status()
        return r
    except requests.exceptions.HTTPError as err:
        return _functions.setModuleError(payload=err, error=r.body['msg'])

def login(user):
    try:
        r = _sUtils.request('/login', {'username': user.username, 'password': user.password}).post()
        r.res.raise_for_status()
        return r
    except requests.exceptions.HTTPError as err:
        return _functions.setModuleError(payload=err, error=r.body['msg'])
