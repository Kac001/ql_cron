'''
new Env('更新财报数据-财报披露计划-增量更新');
UpdateStockDisclosureDate
'''

import requests
from config import sys_config


re = requests.get(sys_config['url']+"/astock/UpdateStockDisclosureDate/?type=1")
print(re.text)