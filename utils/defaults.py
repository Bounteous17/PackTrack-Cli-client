from utils import functions as _functions, auth as _uAuth

api_host = _functions.Config['api']['host']
api_port = _functions.Config['api']['port']
api_url = f'http://{api_host}:{api_port}'

app_config = f'{_functions.userHome()}/.config/thoro'

access_token = {'Authorization': _uAuth.openToken(t_type='access')}
