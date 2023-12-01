'''
new Env('矿机运行检查');
MachineStatusCheckApi
'''

import requests
from config import sys_config


re = requests.get(sys_config['url']+"/coins/MachineStatusCheckApi/")
print(re.text)