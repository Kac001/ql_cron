'''
new Env('更新财报数据-现金流量表-增量更新(根据财报披露计划)');
UpdateStockCashflow
'''

import requests
from config import sys_config


re = requests.get(sys_config['url']+"/astock/UpdateStockCashflow/?type=2")
print(re.text)