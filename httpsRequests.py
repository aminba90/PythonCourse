import requests
import os
import simplejson as json
r=requests.get("https://google.com")
print("status is:",r.status_code)

t=r.headers

print(t)

file = open("./googleHeaders.json","w+")
file.seek(0)
file.write(json.dumps(dict(t)))