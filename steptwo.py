import requests
import json

payload = {"token":"cb4d2e35a6d1ba61efbae8d6273d7e43"}
r = requests.post("http://challenge.code2040.org/api/reverse", json=payload)
toreverse = r.text
payload.update({"string":toreverse[::-1]})
re = requests.post("http://challenge.code2040.org/api/reverse/validate", json=payload)
print re.text
