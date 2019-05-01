class ModuleStatus():
    def __init__(self, **args):
        self.payload = args.get('payload')
        self.error = args.get('error')

class Response():
    def __init__(self, **args):
        self.status = args.get('status')
        self.res = args.get('res')
