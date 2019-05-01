import getpass
from models import user as _modelUser
from services import user as _serviceUser
from utils import functions as _functions

def displaySignup():
    username = input('Username (this information is hidden to the public): ')
    password = getpass.getpass('Password (min 16 chars, max 100 chars): ')
    User = _modelUser.User(username=username, password=password)
    r = _serviceUser.signup(User)
    if _functions.resultError(r):
        return r
    return _functions.setModuleSuccess(payload=r.body['msg'])
