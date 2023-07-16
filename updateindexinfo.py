'''
new Env('更新行情数据-A股指数信息');
updateindexinfo'
'''

import requests
from config import sys_config


re = requests.get(sys_config['url']+"/aindex/updateindexinfo/")
print(re.text)