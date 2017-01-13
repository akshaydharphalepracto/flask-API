import model
from flask import Flask,jsonify,request, Response
app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to CRUD Operations on Helpguide"


@app.route("/document-read/<document_id>" , methods = ['GET'])
def HelpguideRead(document_id):
	json_object = model.readDocument(document_id)
	return jsonify(json_object);

	
	# response = Response(jsonify(json_object), status=200, mimetype='application/json')
	# return response


# @app.route("/student-create/" , methods = ['POST'])
# def StudentCreate():
# 	r_json = request.get_json()
# 	model.createStudent(r_json)
# 	response = Response("Student Created", status=201, mimetype='application/json')
# 	return response


# @app.route("/student-update/<int:student_id>" , methods=['GET'])
# def StudentUpdate(student_id):
# 	r_json = request.get_json()
# 	model.updateStudent(student_id, req_json)
# 	response = Response("Student Updated", status=201, mimetype='application/json')
# 	return response


# @app.route("/student-delete/<int:student_id>", methods=['GET'] )
# def StudentDelete(student_id):
# 	model.deleteStudent(student_id)
# 	response = Response("Student Deleted", status=201, mimetype='application/json')
# 	return response

if __name__ == "__main__":
    app.run(debug=True)