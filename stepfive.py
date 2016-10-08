import requests
import json
from datetime import timedelta, datetime

payload = {"token":"cb4d2e35a6d1ba61efbae8d6273d7e43"}
r = requests.post("http://challenge.code2040.org/api/dating", json=payload)
jsonresp = r.json()
datestamp = jsonresp["datestamp"]
interval = jsonresp["interval"]
date=datetime.strptime(datestamp, "%Y-%m-%dT%H:%M:%S.%f%z") 
date = date+datetime.timedelta(seconds=interval)
payload.update({"datestamp":date.isoformat()})
re = requests.post("http://challenge.code2040.org/api/dating/validate", json=payload)
print re.text
