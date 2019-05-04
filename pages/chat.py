from services import chat as _serviceChat
from utils import functions as _functions
from pages import logged as _pageLogged

def displayInnit():
    username = input('Type the user with whom to start the chat: ')
    r = _serviceChat.innit(username)
    if _functions.resultError(r):
        return r
    _functions.setModuleSuccess(payload=r.body['msg'])

def displayList():
    r = _serviceChat.list()
    if _functions.resultError(r):
        return r
    _functions.setModuleSuccess(payload=r.body)
    return _pageLogged.menu()
