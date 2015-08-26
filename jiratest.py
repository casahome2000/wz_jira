from jira import JIRA
import dateHandler
from dateHandler import MyEncoder
import datetime
import json
import time
from config import ProjectIssues
from account import Creds

dateTODAY = datetime.datetime.now()
jira = JIRA(Creds.JIRA_SITE, basic_auth=(Creds.USER_NAME, Creds.PASSWORD))

createdVersions = []
createdEpics = []

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


def createProject(projectKey, projectName, lead):
	# print('=======================================')
	# print('Creating Project: %s' % projectName)
	new_project = jira.create_project(key=projectKey, name=projectName, assignee=lead)
	# print('Creating the Board for the %s project' % projectName)
	# time.sleep(2)
	jira.create_board(name=projectName, project_ids=[new_project['projectId']])
	new_project_Key = new_project['projectKey']
	# print('Creating the Release Version for the %s project' % projectName)
	# calcStartReleaseDatesForVersions(ProjectIssues.VERSIONS['versions'])
	createVersions(new_project_Key)
	# print('Creating the Epics for the %s project' % projectName)
	createEpicsInProject(new_project_Key)
	# print('=======================================')
	# print('=== Successfully Created %s project ===' % projectName)
	# print('=======================================')
	#TODO: create issues in config file
	#TODO: create issues in the project create_issue
	#TODO: link the issue created to the appropriate epic (may take some refactoring)
	#TODO: write deleteProject()

	return

createProject(projectKey='CAR', projectName='Carlos', lead='admin')












