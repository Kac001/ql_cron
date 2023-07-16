'''
new Env('更新财报数据-主营业务构成-全量更新(更新遗漏&修正数据)');
UpdateStockFinaMainbz_full_fix
'''

import requests
from config import sys_config


re = requests.get(sys_config['url']+"/astock/UpdateStockFinaMainbz/?type=1")
print(re.text)