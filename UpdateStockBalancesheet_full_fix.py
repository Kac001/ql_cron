'''
new Env('更新财报数据-资产负债表-全量更新(更新遗漏&修正数据)');
UpdateStockBalancesheet_full_fix
'''

import requests
from config import sys_config


re = requests.get(sys_config['url']+"/astock/UpdateStockBalancesheet/?type=1")
print(re.text)