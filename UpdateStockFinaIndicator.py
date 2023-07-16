'''
new Env('更新财报数据-财务指标数据-增量更新(根据财报披露计划)');
UpdateStockFinaIndicator
'''

import requests
from config import sys_config


re = requests.get(sys_config['url']+"/astock/UpdateStockFinaIndicator/?type=2")
print(re.text)