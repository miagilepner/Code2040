import requests
import json

payload = {"token":"cb4d2e35a6d1ba61efbae8d6273d7e43"}
r = requests.post("http://challenge.code2040.org/api/prefix", json=payload)
jsonresp = r.json()
prefix = jsonresp["prefix"]
array = jsonresp["array"]
newarray = []
for item in array:
    if not item.startswith(prefix):
        newarray.append(item)
payload.update({"array":newarray})
re = requests.post("http://challenge.code2040.org/api/prefix/validate", json=payload)
print re.text
