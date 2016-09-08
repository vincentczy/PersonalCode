import os
import re
import time

for i in range(5):
    r = os.popen('ping baidu.com')
    text = r.read()
    indices = re.search(r'平均 = (\d+)ms', text).span()
    indices2 = re.search(r'平均 = ', text).span()
    print(text[indices2[1]:indices[1]-2])
    #print(indices)
    r.close
    time.sleep(60)
