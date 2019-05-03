from utils import functions as _functions, defaults as _defaults

def storeTokens(**args):
    try:
        nFile = 'access'
        if args.get('t_type') == 'refresh':
            nFile == 'refresh'
        path=f'{_defaults.app_config}/auth/{nFile}.token.jwt'
        wInst = _functions.openFile(path, 'w+')
        if _functions.resultError(wInst):
            return wInst
        wInst.write(f'Bearer {args.get("token")}')
    except Exception as e:
        _functions.setModuleError(payload=e, error='Error storage tokens')
        exit(1)

def openToken(**args):
    try:
        oFile = 'access'
        if args.get('t_type' == 'refresh'):
            oFile = 'refresh'
        path=f'{_defaults.app_config}/auth/{oFile}.token.jwt'
        rInst = _functions.openFile(path, 'r')
        if _functions.resultError(rInst):
            return rInst
        return rInst.read()
    except Exception as e:
        _functions.setModuleError(payload=e, error='Error looking for the local token')
