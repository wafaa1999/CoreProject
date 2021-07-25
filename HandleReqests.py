from flask import Flask, jsonify, redirect, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app)
cors = CORS(app, resources={
    r"/*": {
        "origins": "*"
    }
})

@app.route('/test', methods=['Get'])
def gg():
    response = row = dict(
            project='Core', )
    return jsonify({'response': response})


@app.route("/loginAuthorization", methods=['GET'])
def redirect_login():
    idUser = request.args.get('idUser')
    password = request.args.get('password')
    url = "https://virtual-grad.herokuapp.com/loginAuthorization"
    url += "?idUser=" + idUser + "&password=" + password
    return redirect(url)


@app.route("/checkAndSendEmail", methods=['GET'])
def redirect_checkAndSendEmail():
    email = request.args.get('email')
    # url = "https://virtual-grad.herokuapp.com/checkAndSendEmail"
    url = "http://127.0.0.1:5000/checkAndSendEmail"
    url += "?email=" + email
    return redirect(url)


@app.route("/getMaterialsOfDepartment", methods=['GET'])
def redirect_getMaterialsOfDepartment():
    idIstructor = request.args.get('idIstructor')
    year = request.args.get('year')
    sem = request.args.get('sem')
    url = "https://virtual-grad.herokuapp.com/getMaterialsOfDepartment"
    url += "?idIstructor=" + idIstructor
    url += "&year=" + year
    url += "&sem=" + sem
    return redirect(url)


@app.route("/getRoomsofDep", methods=['GET'])
def redirect_getRoomsofDep():
    idDep = request.args.get('idDep')
    url = "https://virtual-grad.herokuapp.com/getRoomsofDep"
    # url = "http://127.0.0.1:5000/getRoomsofDep"
    url += "?idDep=" + idDep
    return redirect(url)


@app.route("/editRoom", methods=['GET'])
def redirect_editRoom():
    idDep = request.args.get('idDep')
    number = request.args.get('number')
    campous = request.args.get('campous')
    type = request.args.get('type')
    url = "https://virtual-grad.herokuapp.com/editRoom"
    url += "?idDep=" + idDep
    url += "&number=" + number
    url += "&campous=" + campous
    url += "&type=" + type
    return redirect(url)


@app.route("/addCourseToDepartment", methods=['GET'])
def redirect_addCourseToDepartment():
    idDep = request.args.get('idDep')
    name = request.args.get('name')
    number = request.args.get('number')
    numberOfHour = request.args.get('numberOfHour')
    type = request.args.get('type')
    year = request.args.get('year')
    sem = request.args.get('sem')
    url = "https://virtual-grad.herokuapp.com/addCourseToDepartment?"
    url += "idDep=" + idDep + "&"
    url += "name=" + name + "&"
    url += "number=" + number + "&"
    url += "numberOfHour=" + numberOfHour + "&"
    url += "type=" + type + "&"
    url += "year=" + year + "&"
    url += "sem=" + sem
    return redirect(url)


@app.route("/getAllMaterialsOfDepartment", methods=['GET'])
def redirect_getAllMaterialsOfDepartment():
    idDep = request.args.get('idDep')
    url = "https://virtual-grad.herokuapp.com/getAllMaterialsOfDepartment"
    url += "?idDep=" + idDep
    return redirect(url)


@app.route("/addRoomToDepartment", methods=['GET'])
def addRoomToDepartment():
    idDep = request.args.get('idDep')
    number = request.args.get('number')
    type = request.args.get('type')
    campous = request.args.get('campous')
    url = "https://virtual-grad.herokuapp.com/addRoomToDepartment"
    url += "?idDep=" + idDep
    url += "&number=" + number
    url += "&type=" + type
    url += "&campous=" + campous
    return redirect(url)

@app.route("/deleteRoomFromDep", methods=['GET'])
def deleteRoomFromDep():
    idDep = request.args.get('idDep')
    number = request.args.get('number')
    url = "https://virtual-grad.herokuapp.com/deleteRoomFromDep"
    url += "?idDep=" + idDep
    url += "&number=" + number
    return redirect(url)





if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3002)
