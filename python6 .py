#避免转义给字符串加哪个字母表示原始字符串？

import re

str = '<div class = "nam">中国</div>'

res = re.findall(r'<div class = ".*">(.*?)</div>',str)

print(res)