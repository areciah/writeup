import requests

res = requests.get("http://war.sschall.xyz:1713/level1/p6/index.html")
print(res.text)