# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
import json

url = "https://jira-hostingupdate.it-economics-testing.de/rest/api/2/project/type"

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json",
  "Authorization": "Bearer OTY2MDcxNzQ0NjYyOj8GfA6V1h/+bZUeHYmPHrTqZZx+"
}

response = requests.request(
   "GET",
   url,
   headers=headers
)
#print(json.loads(response.text))
print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))