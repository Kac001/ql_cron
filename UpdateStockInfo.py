'''
更新基础数据-A股基础信息
UpdateStockInfo
'''

import requests
from config import sys_config


re = requests.get(sys_config['url']+"/astock/UpdateStockInfo/")
print(re.text)