'''
new Env('推送发行日历');
CbIssueCalendarPushApi
'''

import requests
from config import sys_config


re = requests.get(sys_config['url']+"/acb/CbIssueCalendarPushApi/")
print(re.text)