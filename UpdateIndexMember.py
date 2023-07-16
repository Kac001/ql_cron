'''
new Env('更新行情数据-申万行业成分构成');
UpdateIndexMember
'''

import requests
from config import sys_config


re = requests.get(sys_config['url']+"/aindex/UpdateIndexMember/")
print(re.text)