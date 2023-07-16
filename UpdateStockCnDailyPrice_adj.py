'''
new Env('更新行情数据-A股日线复权因子');
UpdateStockCnDailyPrice_adj
'''

import requests
from config import sys_config


re = requests.get(sys_config['url']+"/astock/UpdateStockCnDailyPrice/?type=4")
print(re.text)