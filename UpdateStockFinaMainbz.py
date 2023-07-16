'''
new Env('更新财报数据-主营业务构成-增量更新(根据财报披露计划)');
UpdateStockFinaMainbz
'''

import requests
from config import sys_config


re = requests.get(sys_config['url']+"/astock/UpdateStockFinaMainbz/?type=2")
print(re.text)