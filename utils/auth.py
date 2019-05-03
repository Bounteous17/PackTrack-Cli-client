from utils import functions as _functions

def storeTokens(**args):
    try:
        nFile = 'access'
        if args.get('t_type') == 'refresh':
            nFile == 'refresh'
        path=f'{_functions.userHome()}/.config/thoro/auth/{nFile}.token.jwt'
        wInst = _functions.openFile(path, 'w+')
        if _functions.resultError(wInst):
            return wInst
        wInst.write(f'Bearer {args.get("token")}')
    except Exception as e:
        _functions.setModuleError(payload=e, error='Error storage tokens')
        exit(1)
