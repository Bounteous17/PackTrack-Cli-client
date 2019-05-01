import os
from pages import login as _pageLogin, signup as _pageSignup
from utils import colorize as _colorize

def display():
    print ("""
            [1] - Login
            [2] - Signup
            [3] - Get all user private info
            [0] - Exit
            """)
def welcome():
    _colorize.consoleLog(action='info', msg='\nWelcome to Thori, the secure and private messaging APP')
def select():
    welcome()
    ans = True
    while ans:
        display()
        ans = input('Select option: ')
        if ans == '1':
            _pageLogin.displayLogin()
        if ans == '2':
            _pageSignup.displaySignup()
        elif ans == '0':
            exit(0)
        else:
            _colorize.consoleLog(action='error', msg='Unknown option, exit')
            exit(1)
