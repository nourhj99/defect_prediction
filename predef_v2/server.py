from flask import Flask, request,jsonify
from predef_v2.driver.driver import *


app = Flask(__name__)



@app.route('/analyse')
def analyse():
	data = request.get_json()
	git_url = data['git_repo']
	project  = Project(git_url)
	project.clone()
	project.explore_project()
	project.analyze()
	project.compute_overall_results()
	print(project.globalToJson())
	return project.globalToJson()



if __name__ == "__main__":
    app.run(host="0.0.0.0",port=3030,debug = False)	