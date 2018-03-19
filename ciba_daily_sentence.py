import urllib.request
import json
import re
import time

#base_url = "http://sentence.iciba.com/index.php?callback=jQuery19007661007067399854_1521446862726&c=dailysentence&m=getdetail&title=2018-03-19&_=1521446862000"

base_url = "http://sentence.iciba.com/index.php?c=dailysentence&m=getdetail&"

time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
date = {
    "title":time
}

date = urllib.parse.urlencode(date)
url = "".join((base_url, date))
response = urllib.request.urlopen(url)

raw_content = response.read().decode("utf-8")

#用正则找到http返回值中的json字符串
json_content = re.search(r"\{.*\}", raw_content).group(0)

#将json转换成dict
content_dict = json.loads(json_content)


print(content_dict["translation"])
print(content_dict["content"])
