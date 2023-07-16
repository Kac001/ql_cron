'''
new Env('更新财报数据-利润表-增量更新(根据财报披露计划)');
UpdateStockIncome
'''

import requests
from config import sys_config


re = requests.get(sys_config['url']+"/astock/UpdateStockIncome/?type=2")
print(re.text)