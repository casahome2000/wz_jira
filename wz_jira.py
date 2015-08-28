from flask import Flask, redirect, request, url_for, render_template, flash, make_response
import jiratest


app = Flask(__name__)
app.secret_key = 'weezlabsRulz'


@app.route('/newproject', methods=['GET','POST'])
def makeProject():

	if request.method =="POST":
		if len(request.form) < 3:
			flash("ERROR: Please fill in all the fields")
			return render_template('forms/newproject.html')

		key = request.form['projectKey']
		name = request.form['projectName']
		lead = request.form['projectManager']

		if jiratest.checkIfProject(key):
			flash("ERROR: Project Key exists in Jira, unable to cretae project")
			return render_template('forms/newproject.html')
		else:
			flash("INFO: Creating project in Jira....")


		jiratest.createProject(projectKey=key, projectName=name, lead=lead)
		flash("SUCCESS: Project created")

		return render_template('forms/newproject.html')
	else:
		flash("INFO: Welcome to the WeezLabs Custom PMO portal")
		return render_template('forms/newproject.html')




	return render_template('forms/newproject.html')


if __name__ == '__main__':
	app.run(debug=True)
