'''
new Env('更新财报数据-财务指标数据-全量更新(更新遗漏&修正数据)');
UpdateStockFinaIndicator_full_fix
'''

import requests
from config import sys_config


re = requests.get(sys_config['url']+"/astock/UpdateStockFinaIndicator/?type=1")
print(re.text)