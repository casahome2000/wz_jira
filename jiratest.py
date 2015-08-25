from jira import JIRA
import dateHandler
from dateHandler import MyEncoder
import datetime
import json
from config import ProjectIssues

dateTODAY = datetime.datetime.now()
jira = JIRA('https://weezlabs.atlassian.net', basic_auth=('admin', 'W11z_Labs'))


projects = jira.projects()
print("Number of Projects: ", len(projects))
for project in projects:
	print('Project Name: ', project)



createdVersions=[]
createdEpics=[]

def createEpicsInProject(projKey):
	epics = ProjectIssues.EPICS['phases']
	for phase in epics:
		fields = {
			'project': {
				'key': projKey
			},
			'summary': phase['summary'],
			'description': phase['description'],
			'issuetype': {
				'name': 'Epic'
			},
			"customfield_10008": phase['name'],  #this is EpicName
			'priority': {
				'name': 'Highest'
			},
			'fixVersions': [{
				'name': phase['fixversion']
			}]
		}

		issue = jira.create_issue(fields=fields)
		createdEpics.append(issue)

	return

def createVersions(projKey):

	versions = ProjectIssues.VERSIONS['versions']
	for version in versions:

		newVersion = jira.create_version(name=version['name'],
										 project=projKey,
										 startDate=version['startdate'],
										 releaseDate=version['releasedate'],
										 description=version['description'])
		createdVersions.append(newVersion)

	return



def createProject(projectKey, projectName, lead):

	new_project = jira.create_project(key=projectKey, name=projectName, assignee=lead)
	jira.create_board(name=projectName, project_ids=[new_project['projectId']])
	new_project_Key = new_project['projectKey']

	createVersions(new_project_Key)
	createEpicsInProject(new_project_Key)
	#TODO: create issues in config file
	#TODO: create issues in the project create_issue
	#TODO: link the issue created to the appropriate epic (may take some refactoring)
	#TODO: figure out StartDate and ReleaseDate for Versions (may take some refactoring)

	return

createProject(projectKey='NEW', projectName='My New Project', lead='admin')





# jira.add_issues_to_epic('epicID','issue_keys')
# jira.create_issue()







