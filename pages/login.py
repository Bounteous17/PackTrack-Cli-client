import getpass
from models import user as _modelUser
from services import user as _serviceUser
from utils import functions as _functions

def displayLogin():
    username = input('Username: ')
    password = getpass.getpass('Password: ')
    User = _modelUser.User(username=username, password=password)
    r = _serviceUser.login(User)
    if _functions.resultError(r):
        return r
    return _functions.setModuleSuccess(payload=r.body['msg'])
