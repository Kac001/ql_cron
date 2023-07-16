'''
new Env('更新特色数据-券商每月荐股');
UpdateStockBrokerRecommend
'''

import requests
from config import sys_config


re = requests.get(sys_config['url']+"/astock/UpdateStockBrokerRecommend/?type=1")
print(re.text)