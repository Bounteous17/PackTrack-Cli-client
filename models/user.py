class User():
    def __init__(self, **args):
        self.id = args.get('id')
        self.username = args.get('username')
        self.password = args.get('password')

