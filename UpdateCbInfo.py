'''
new Env('更新基础数据-可转债基础信息');
UpdateCbInfo
'''

import requests
from config import sys_config


re = requests.get(sys_config['url']+"/acb/UpdateCbInfo/")
print(re.text)