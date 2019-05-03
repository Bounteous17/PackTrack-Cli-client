from utils import colorize as _colorize

def menu():
    ans = True
    while ans:
        print("""
            [1] - Start new chat
            [0] - Logout
        """)
        ans = input('Select option: ')
        if ans == '1':
            startChat()
        elif ans == '0':
            _colorize.consoleLog(action='success', msg='\nUser logout success')
            ans = False
        else:
            _colorize.consoleLog(action='error', msg='\nUnknown option for logged user')

def startChat():
    nUsername = input('Enter Username for new chat: ')

