'''
new Env('矿机收益检查');
MiningProfitCheckApi
'''

import requests
from config import sys_config


re = requests.get(sys_config['url']+"/coins/MiningProfitCheckApi/")
print(re.text)