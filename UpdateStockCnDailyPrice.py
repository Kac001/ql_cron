'''
new Env('更新行情数据-A股指数价格');
UpdateStockCnDailyPrice
'''

import requests
from config import sys_config


re = requests.get(sys_config['url']+"/astock/UpdateStockCnDailyPrice/?type=2")
print(re.text)