import json
from utils import colorize as _colorize
from ruamel.yaml import YAML
from models import rest as _rest

def setModuleError(**args):
    _colorize.consoleLog(action='warning', msg=f'\n{args.get("payload")}')
    _colorize.consoleLog(action='error', msg=f'{args.get("error")}\n')
    return _rest.ModuleStatus(payload=args.get('payload'), error=args.get('error'))

def setModuleSuccess(**args):
    _colorize.consoleLog(action='success', msg=f'\n{args.get("payload")}\n')
    return _rest.ModuleStatus(payload=args.get('payload'))

def resultError(result):
    if isinstance(result, _rest.ModuleStatus) and result.error:
        return True
    return False

def getConfig():
    try:
        readYamlConfig = readFile("./config/config.yaml", 'r')
        if resultError(readYamlConfig):
            return readYamlConfig

        yamlconfig = readYamlConfig
        config = YAML().load(yamlconfig)
        return config
    except Exception as e:
        return setModuleError(payload=e, error='Error reading config file')

def readFile(path, perms):
    try:
        if not perms:
            perms = 'r'
        f = open(path, perms)
        return f.read()
    except Exception as e:
        return setModuleError(payload=e, error='RAW file can\'t be accessed at the moment')

def encodeJson(res):
    return json.loads(res)

Config = getConfig()
