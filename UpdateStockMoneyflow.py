'''
new Env('更新行情数据-中国A股资金流向');
UpdateStockMoneyflow
'''

import requests
from config import sys_config


re = requests.get(sys_config['url']+"/astock/UpdateStockMoneyflow/?type=2")
print(re.text)