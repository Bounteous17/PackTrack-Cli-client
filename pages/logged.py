from utils import colorize as _colorize
from pages import chat as _pageChat

def menu():
    ans = True
    while ans:
        print("""
            [1] - Start new chat
            [2] - List chats
            [0] - Logout
        """)
        ans = input('Select option: ')
        if ans == '1':
            _pageChat.displayInnit()
        elif ans == '2':
            _pageChat.displayList()
        elif ans == '0':
            _colorize.consoleLog(action='success', msg='\nUser logout success')
            ans = False
        else:
            _colorize.consoleLog(action='error', msg='\nUnknown option for logged user')

