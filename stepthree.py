import requests
import json

payload = {"token":"cb4d2e35a6d1ba61efbae8d6273d7e43"}
r = requests.post("http://challenge.code2040.org/api/haystack", json=payload)
jsonresp = r.json()
needle = jsonresp["needle"]
haystack = jsonresp["haystack"]
index = haystack.index(needle)
payload.update({"needle":index})
re = requests.post("http://challenge.code2040.org/api/haystack/validate", json=payload)
print re.text
