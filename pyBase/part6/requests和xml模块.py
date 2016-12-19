# -*- coding:utf-8 -*-
# Author:YEAR
import requests

response = requests.get("http://www.baidu.com")
response.encoding = "utf-8"
result = response.text
print(result)

from xml.etree import ElementTree as ET

r = requests.get('biubiuiu')
result = r.text
root = ET.XML(result)

for node in root.iter('biubiubiu'):
    print(node.tag, node.attrib)
    print(node.find('biubiu').text)

tree = ET.parse('baba.xml')
root = tree.getroot()
# 修改root
root.write('output.xml')
