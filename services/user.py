import requests
from utils import functions as _functions, defaults as _defaults
from services import utils as _sUtils

def signup(user):
    try:
        r = _sUtils.request(endpoint='/signup', body={'username': user.username, 'password': user.password}).post()
        r.res.raise_for_status()
    except requests.exceptions.HTTPError as err:
        _functions.setModuleError(payload=err, error=r.body['msg'])
        sys.exit(1)
