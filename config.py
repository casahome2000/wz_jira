__author__ = 'casahome2000'
import dateHandler


def calcReleaseDate(prevRelease, currentDuration):
	date = dateHandler.date_by_adding_business_days(dateHandler.datetime.datetime(dateHandler.dateTODAY.year,
																				  dateHandler.dateTODAY.month,
																				  dateHandler.dateTODAY.day),
													10,
													dateHandler.Holidays)
	releaseDate = "%s-%s-%s" % (date.year, date.month, date.day)
	return releaseDate


class ProjectIssues(object):

	EPICS = {
		"phases": [
			dict(name="Phase 1: Kick Off",
				 description='The kick-off meeting will allow the UX and PM get a foothold on what the client is trying to ' \
							 'accomplish. The PM, UX, and Sales will meet with the client, and review the LEAN CANVAS provided by ' \
							 'sales to the assigned pre-development team before the meeting. This should facilitate the completion ' \
							 'of the Kick-Off Meeting Form, which should be the output from the conclusion of the kick-off meeting. ' \
							 'At this point, enough information should be provided by the client for the team to proceed to Phase 2',
				 summary="Kick Off",
				 fixversion="Phase 1: Kick Off",
				 durration=2),
			dict(name="Phase 2: Competitive Analysis",
				 description="The Competitive Analysis phase will allow the PM and UX define the strategy for the client's " \
							 "application. It will include comprehensive research on what apps are already filling the " \
							 "competitive space, identify what needs and gaps to fill, identify the user personas, and " \
							 "ultimately present to the client the direction the pre-development team feels will provide " \
							 "the best MVP. The PM will initially support the UX by providing research documentation, which " \
							 "will be compiled into a presentation for the client to easily absorb our strategy. It will " \
							 "also produce the groomed Feature List for sign-off with the client. These will ultimately dictate " \
							 "the needed materials to proceed to [Phase III - UX Flow]. Lastly, the client will need to fill " \
							 "out the [Creative Brief] at this point, and be given 2-3 days to complete.",
				 summary="Competitive Analysis",
				 fixversion="Phase 2: Competitive Analysis",
				 durration=5),
			dict(name="Phase 3: UX Flow",
				 description="The UX should now have enough information to begin creating the UX Flow document. Within that " \
							 "period, the PM will proceed to groom the schedule and tickets to ensure the project is " \
							 "staying on track. At the final stage of this phase, the client will review the UX Flow and " \
							 "updated schedule. This phase will require [Milestone Sign-Off] for the UX Flow before proceeding " \
							 "to the next stage: [Phase IV - Wireframes]. Sign off can be approved by e-mail with the client," \
							 " or they can come in for a meeting if they choose to. Please account for meeting hours if the " \
							 "client comes in for review.",
				 summary="UX Flow",
				 fixversion="Phase 3: UX Flow",
				 durration=7),
			dict(name="Phase 4: Wireframes",
				 description="The UX designer now has full project scope in hand, which has been reviewed and signed-off on " \
							 "by the client. This phase defines the project from low-mid fidelity, with the output being " \
							 "fully clickable, partially annotated wireframes to be passed on to the designers for " \
							 "[Phase V - Preliminary Designs]. Additionally, the PM will parallel path, and begin " \
							 "[Phase VI - Annotations and Developer Review]. This will provide comprehensive material and " \
							 "project scope to both verticals to begin the first real preparations for development. " \
							 "Client must approve of this milestone with the [Milestone Sign-Off].",
				 summary="Wireframes",
				 fixversion="Phase 4: Wireframes",
				 durration=15),
			dict(name="Phase 5: Preliminary Designs",
				 description="The preliminary designs will allow the client to choose from 3 alternative designs, " \
							 "from 2 wireframe screens. The client will review, and provide feedback leading to " \
							 "final approval of the overall design direction, which will lead into " \
							 "[Phase VII - Full Design].",
				 summary="Preliminary Designs",
				 fixversion="Phase 5: Preliminary Designs",
				 durration=10),
			dict(name="Phase 6: Annotations and Developer Review",
				 description="This phase will run parallel to [Phase VII - Full Design]. It will serve as the " \
							 "kick-off point to begin project awareness with the developer team. The annotated " \
							 "wireframes should be enough to provide an overview of the application and its " \
							 "functionality to the development teams, and get their assessment of what solutions we " \
							 "will need to consider to get this project into development. Final objective is to make " \
							 "the development team aware of the project, have a good reference document for them to " \
							 "assess project needs, and begin quote production at an early stage for full preparation " \
							 "at [Phase VIII - Project Wrap].",
				 summary="Annotations and Developer Review",
				 fixversion="Phase 6: Annotations and Developer Review",
				 durration=7),
			dict(name="Phase 7: Full Design",
				 description="Full design. Designers flesh out the remaining application based on the approved " \
							 "direction set by [Phase V - Preliminary Designs]. The final output will be the full " \
							 "designed application based on the wireframes, with a full, clickable prototype. " \
							 "This is the final stage of pre-development, but leads to [Phase VIII - Project Wrap], " \
							 "which produces the development quote and pitch for the client to move on to development.",
				 summary="Full Design",
				 fixversion="Phase 7: Full Designs",
				 durration=20),
			dict(name="Phase 8: Project Wrap",
				 description="This is the final stage. Asset delivery, and the final quote to the client for " \
							 "development. Any additional follow up and project grooming that needs to take.",
				 summary="Project Wrap",
				 fixversion="Phase 8: Project Wrap",
				 durration=2)
		]
	}

	VERSIONS = {
		"versions": [
			dict(name="Phase 1: Kick Off",
				 description="Kick Off",
				 startdate=(
					 "%s-%s-%s" % (dateHandler.dateTODAY.year, dateHandler.dateTODAY.month, dateHandler.dateTODAY.day)),
				 releasedate=None,
				 duration=2),
			dict(name="Phase 2: Competitive Analysis",
				 description="Competitive Analysis",
				 startdate=None,
				 releasedate=None,
				 duration=5),
			dict(name="Phase 3: UX Flow",
				 description="UX Flow",
				 startdate=None,
				 releasedate=None,
				 duration=7),
			dict(name="Phase 4: Wireframes",
				 description="Wireframes",
				 startdate=None,
				 releasedate=None,
				 duration=15),
			dict(name="Phase 5: Preliminary Designs",
				 description="Preliminary Designs",
				 startdate=None,
				 releasedate=None,
				 duration=10),
			dict(name="Phase 6: Annotations and Developer Review",
				 description="Annotations and Developer Review",
				 startdate=None,
				 releasedate=None,
				 duration=7),
			dict(name="Phase 7: Full Designs",
				 description="Full Designs",
				 startdate=None,
				 releasedate=None,
				 duration=20),
			dict(name="Phase 8: Project Wrap",
				 description="Project Wrap",
				 startdate=None,
				 releasedate=None,
				 duration=2)
		]
	}
	ISSUES = {
		"issues": [
			dict(name="Phase 1: Kick Off",
				 description="Kick Off",
				 startdate=(
					 "%s-%s-%s" % (dateHandler.dateTODAY.year, dateHandler.dateTODAY.month, dateHandler.dateTODAY.day)),
				 releasedate=None,
				 duration=2),
			dict(name="Phase 2: Competitive Analysis",
				 description="Competitive Analysis",
				 startdate=None,
				 releasedate=None,
				 duration=5),
			dict(name="Phase 3: UX Flow",
				 description="UX Flow",
				 startdate=None,
				 releasedate=None,
				 duration=7),
			dict(name="Phase 4: Wireframes",
				 description="Wireframes",
				 startdate=None,
				 releasedate=None,
				 duration=15),
			dict(name="Phase 5: Preliminary Designs",
				 description="Preliminary Designs",
				 startdate=None,
				 releasedate=None,
				 duration=10),
			dict(name="Phase 6: Annotations and Developer Review",
				 description="Annotations and Developer Review",
				 startdate=None,
				 releasedate=None,
				 duration=7),
			dict(name="Phase 7: Full Designs",
				 description="Full Designs",
				 startdate=None,
				 releasedate=None,
				 duration=20),
			dict(name="Phase 8: Project Wrap",
				 description="Project Wrap",
				 startdate=None,
				 releasedate=None,
				 duration=2)
		]
	}





