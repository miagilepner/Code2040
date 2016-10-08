import requests

payload = {"token":"cb4d2e35a6d1ba61efbae8d6273d7e43", "github":"https://github.com/miagilepner/Code2040"}
r = requests.post("http://challenge.code2040.org/api/register", json=payload)
print r.text
