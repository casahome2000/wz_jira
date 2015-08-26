from jira import JIRA
import dateHandler
from dateHandler import MyEncoder
import datetime
import json
from config import ProjectIssues
from account import Creds

dateTODAY = datetime.datetime.now()
jira = JIRA(Creds.JIRA_SITE, basic_auth=(Creds.USER_NAME, Creds.PASSWORD))

createdEpics = []

def convertHoursToSeconds(hours):
	seconds = (hours*60)*60
	return seconds

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
			"customfield_10008": phase['name'],  # this is EpicName
			'priority': {
				'name': 'Highest'
			},
			'fixVersions': [{
								'name': phase['fixversion']
							}]
		}

		issue = jira.create_issue(fields=fields)
		createdEpics.append(issue.key)

	return


def createVersions(projKey):
	versions = ProjectIssues.VERSIONS['versions']
	for version in versions:
		newVersion = jira.create_version(name=version['name'],
										 project=projKey,
										 startDate=version['startdate'],
										 releaseDate=version['releasedate'],
										 description=version['description'])

	return

def createIssues(projKey):
	issues = ProjectIssues.ISSUES['issues']
	for issue in issues:
		issue_dict = {
			'project': {'key': projKey},
			'summary': issue['summary'],
    		'description': issue['description'],
    		'issuetype': {'name': 'Story'},
			'fixVersions': [{
								'name': issue['fixversion'] #needs to be the name of the version
							}]
			# 'timeoriginalestimate':convertHoursToSeconds(issue['duration'])
		}

		newIssue = jira.create_issue(fields=issue_dict)
		#TODO: the below if/elif should be in a function and refactored (not efficient)
		if issue['epic'] == 1:
			jira.add_issues_to_epic(createdEpics[0],[newIssue.key])
			continue
		elif issue['epic'] == 2:
			jira.add_issues_to_epic(createdEpics[1],[newIssue.key])
			continue
		elif issue['epic'] == 3:
			jira.add_issues_to_epic(createdEpics[2],[newIssue.key])
			continue
		elif issue['epic'] == 4:
			jira.add_issues_to_epic(createdEpics[3],[newIssue.key])
			continue
		elif issue['epic'] == 5:
			jira.add_issues_to_epic(createdEpics[4],[newIssue.key])
			continue
		elif issue['epic'] == 6:
			jira.add_issues_to_epic(createdEpics[5],[newIssue.key])
			continue
		elif issue['epic'] == 7:
			jira.add_issues_to_epic(createdEpics[6],[newIssue.key])
			continue
		elif issue['epic'] == 8:
			jira.add_issues_to_epic(createdEpics[7],[newIssue.key])
			continue
		else:
			continue
	return


def calcStartReleaseDatesForVersions(versions):
	"""
	calculates the Start/Release Dates for VERSIONS and sets them back to the obj
	:param versions: list of dicts
	:return:
	"""

	lastReleaseDate = ""
	for index, version in enumerate(versions):
		if index == 0:
			duration = int(version['duration'])
			releaseFull = dateHandler.date_by_adding_business_days(datetime.datetime(dateTODAY.year, dateTODAY.month, dateTODAY.day),duration,dateHandler.Holidays)
			releaseDate = ("%s-%s-%s" % (releaseFull.year, releaseFull.month, releaseFull.day))

			lastReleaseDate= releaseDate
			version['releasedate'] = releaseDate
		else:
			version['startdate'] = lastReleaseDate #set startdate for this version
			duration = int(version['duration'])
			startYear = int(lastReleaseDate[:4]) #year as int
			startMonth = (int(lastReleaseDate.partition('-')[-1].rpartition('-')[0])) #month as int
			startDay = (int(lastReleaseDate.rpartition('-')[-1])) #day as int
			releaseFull = dateHandler.date_by_adding_business_days(datetime.datetime(startYear, startMonth, startDay),duration,dateHandler.Holidays)
			releaseDate = ("%s-%s-%s" % (releaseFull.year, releaseFull.month, releaseFull.day))

			lastReleaseDate = releaseDate
			version['releasedate'] = releaseDate

	return

def deleteProject(projectKey):
	#TODO: add user option to abort IF don't want to delete project
	return jira.delete_project(projectKey)

def createProject(projectKey, projectName, lead):

	if deleteProject(projectKey):
		print("% project exists: PROJECT DELETED" % projectName)

	print('=======================================')
	print('Creating Project: %s' % projectName)
	new_project = jira.create_project(key=projectKey, name=projectName, assignee=lead)
	print('Creating the Board for the %s project' % projectName)
	jira.create_board(name=projectName, project_ids=[new_project['projectId']])
	new_project_Key = new_project['projectKey']
	print('Creating the Release Version for the %s project' % projectName)
	calcStartReleaseDatesForVersions(ProjectIssues.VERSIONS['versions'])
	createVersions(new_project_Key)
	print('Creating the Epics for the %s project' % projectName)
	createEpicsInProject(new_project_Key)
	print('Creating the Issues for the %s project (this may take some time)' % projectName)
	createIssues(new_project_Key) #could be done in multi-thread but really...it's a script
	print('=======================================')
	print('=== Successfully Created %s project ===' % projectName)
	print('=======================================')

	#TODO: create ticket with Atlassian for orphaned board after project delete (cause=delete_board method does not remove)
	#TODO: create ticket with Atlassian for API not allowing timeoriginalestimate via REST calls for issues
	#TODO: create ticket with Atlassian for API not allowing interrogation of boards (change est to hrs from points)

	return

createProject(projectKey='CODY', projectName='Cody', lead='admin')
















