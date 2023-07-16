'''
new Env('更新特色数据-小佩估值因子');
UpdateStockVx
'''

import requests
from config import sys_config


re = requests.get(sys_config['url']+"/astock/UpdateStockVx/?type=0&start_date=20230101&end_date=20230405")
print(re.text)