import requests
import json
import subprocess

#https://bitbucket-drvtwo.it-economics-testing.de/
# Auth BBDC-MTM0ODUyODc2Njk4Ot2wn5UNkVFk/v6IWcXzfltlAv6M
#https://bitbucket.it-economics.de/
# Auth

urlorigin = 'https://bitbucket.it-economics.de/'
### API Endpoint to get all projects for Bitbucket server
urlApiProjects = f"{urlorigin}rest/api/latest/projects"
api_token = "BBDC-NDI0NTQ0MzgxNTk0OnekH92qKZ2wuGtO9favEpW2diIj"
#Populate Projects data in list
projectsNeedInfo = []
# All info from Projects in raw json
#allProjectsListInfo = []

# Get all Projects with API endpoint and return json
def get_all_project_json(api_endpoint, token):
    headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {token}"
    }

    response = requests.request(
    "GET",
    api_endpoint,
    headers=headers
    )

    return json.loads(response.text)


def get_project_info(projectDataJson):
  for projectInfo in projectDataJson['values']:

    # Store project: name, key, desc and repos in dictionary
    project = {}
    
    project.update({'name':projectInfo['name']})
    project.update({'key':projectInfo['key']})
    project.update({'repos':[]})

    projectKey = projectInfo['key']

    url = f'{urlorigin}rest/api/latest/projects/{projectKey}/repos'

    headers = {
    "Accept": "application/json",
    "Authorization": "Bearer {token}"
    }
    response = requests.request(
     "GET",
     url,
     headers=headers
    )

    repoDataJson = json.loads(response.text)
    
    try:
      for repovalue in repoDataJson['values']:

       repoSlug = repovalue['slug']
       projectLowerCase = projectKey.lower()
       repourl = f'{urlorigin}scm/{projectLowerCase}/{repoSlug}.git'
       
       project['repos'].append(repourl)
       #print(repourl)
       
    except:
      print("No access to repository")

    # You store all gathered data for the project in a List  
    projectsNeedInfo.append(project)
    

def iterate_gathered_project_data(projectGatheredInfoList):

    for index in range(len(projectGatheredInfoList)):
    
        everyProject = projectsNeedInfo[index]

        
        # Create project in bitbucket
        projectName = everyProject['name']
        projectKey = everyProject['key']

        try:
            projectName = everyProject['description']
        except:
            print("No description")
            print(projectName)
        reposList = everyProject.get("repos")
        
        #TODO! Create repos in Project
        for repoUrl in reposList:
            print(repoUrl)

## Store project info from API endpoint in 
datajson = get_all_project_json(urlApiProjects, api_token)

get_project_info(datajson)

iterate_gathered_project_data(projectsNeedInfo)
