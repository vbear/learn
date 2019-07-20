import requests
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

respone = requests.get("https://prometheus.io/download/", headers=headers)

# print respone.text

pattern = re.compile(r'<td class="filename"><a class="download" href=".*?\.gz"', re.S)

basic_content = re.findall(pattern, respone.text)

for i in basic_content:
    print "wget", i.split()[3][6:-1]
