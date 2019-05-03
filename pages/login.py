import getpass
from models import user as _modelUser
from services import user as _serviceUser
from utils import functions as _functions, auth as _uAuth
from pages import logged as _pageLogged

def displayLogin():
    username = input('Username: ')
    password = getpass.getpass('Password: ')
    User = _modelUser.User(username=username, password=password)
    r = _serviceUser.login(User)
    if _functions.resultError(r):
        return r
    _functions.setModuleSuccess(payload=r.body['msg'])
    _uAuth.storeTokens(t_type='access', token=r.body['access_token'])
    return _pageLogged.menu()
