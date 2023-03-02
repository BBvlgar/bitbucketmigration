# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
import json

baseurl = ""
repoName = ""
repoSlug = ""
projectProj = ""

url = "http://{baseurl}/rest/api/latest/projects/{projectKey}/repos"

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "name": f"{repoName}",
  "scmId": "git",
  "slug": f"{repoSlug}",
  "project": f"{projectProj}",
  "links": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))