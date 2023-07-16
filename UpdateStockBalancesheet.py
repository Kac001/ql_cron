'''
new Env('更新财报数据-资产负债表-增量更新(根据财报披露计划)');
UpdateStockBalancesheet
'''

import requests
from config import sys_config


re = requests.get(sys_config['url']+"/astock/UpdateStockBalancesheet/?type=2")
print(re.text)