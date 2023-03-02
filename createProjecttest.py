# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
import json
import base64

userpass = "admin" + ':' + "Def123"
encoded_u = base64.b64encode(userpass.encode()).decode()

baseurl = "https://bitbucket-drvtwo.it-economics-testing.de"

url = f"{baseurl}/rest/api/latest/projects"


token = "BBDC-MTM0ODUyODc2Njk4Ot2wn5UNkVFk/v6IWcXzfltlAv6M"

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json",
  "Authorization": f"Basic {encoded_u}"
}

payload = json.dumps( {
  "key": "Pol",
  "name": "Pol Repo",
  "description": "This is a short test description Pol repo with the python script"
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))