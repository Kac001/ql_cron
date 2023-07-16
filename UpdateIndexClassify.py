'''
new Env('更新基础数据-申万行业分类');
UpdateIndexClassify
'''

import requests
from config import sys_config


re = requests.get(sys_config['url']+"/aindex/UpdateIndexClassify/")
print(re.text)