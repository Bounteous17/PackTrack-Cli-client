from utils import functions as _functions

api_host = _functions.Config['api']['host']
api_port = _functions.Config['api']['port']
api_url = f'http://{api_host}:{api_port}'
