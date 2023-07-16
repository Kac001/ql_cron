'''
new Env('更新行情数据-中国A股每日指标');
UpdateStockDailyBasic
'''

import requests
from config import sys_config


re = requests.get(sys_config['url']+"/astock/UpdateStockDailyBasic/")
print(re.text)