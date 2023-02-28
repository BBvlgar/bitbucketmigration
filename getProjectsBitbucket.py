# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
import json

url = "https://bitbucket-hostingupdate.it-economics-testing.de/rest/api/latest/projects"

headers = {
  "Accept": "application/json",
  "Authorization": "Bearer BBDC-Njg5MDg2Mzk4ODU2Oo53SHP3pISt1pnIkR9B5C3j4pDb"
}

response = requests.request(
   "GET",
   url,
   headers=headers
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
  
