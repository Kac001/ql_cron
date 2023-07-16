'''
new Env('修复因子缺失');
UpdateStockCnDailyPrice_fix_adj
'''

import requests
from config import sys_config


re = requests.get(sys_config['url']+"/UpdateStockCnDailyPrice/?type=5")
print(re.text)