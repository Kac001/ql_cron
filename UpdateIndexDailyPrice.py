'''
new Env('更新行情数据-A股日线数据');
UpdateStockCnDailyPrice
'''

import requests
from config import sys_config


re = requests.get(sys_config['url']+"/aindex/UpdateIndexDailyPrice/?type=2")
print(re.text)