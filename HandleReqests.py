from flask import Flask, jsonify, redirect, request

app = Flask(__name__)


@app.route("/loginAuthorization", methods=['GET'])
def redirect_login():
    idUser = request.args.get('idUser')
    password = request.args.get('password')
    url = "http://192.168.1.7:3000/loginAuthorization"
    url += "?idUser=" + idUser + "&password=" + password
    return redirect(url)


@app.route("/checkAndSendEmail", methods=['GET'])
def redirect_checkAndSendEmail():
    email = request.args.get('email')
    url = "http://192.168.1.7:3000/checkAndSendEmail"
    url += "?email=" + email
    return redirect(url)


@app.route("/getMaterialsOfDepartment", methods=['GET'])
def redirect_getMaterialsOfDepartment():
    idIstructor = request.args.get('idIstructor')
    year = request.args.get('year')
    sem = request.args.get('sem')
    url = "http://192.168.1.7:3000/getMaterialsOfDepartment"
    url += "?idIstructor=" + idIstructor
    url += "&year=" + year
    url += "&sem=" + sem
    return redirect(url)


@app.route("/getRoomsofDep", methods=['GET'])
def redirect_getRoomsofDep():
    idDep = request.args.get('idDep')
    url = "http://192.168.1.7:3000/getRoomsofDep"
    url += "?idDep=" + idDep
    return redirect(url)


@app.route("/editRoom", methods=['GET'])
def redirect_editRoom():
    idDep = request.args.get('idDep')
    number = request.args.get('number')
    campous = request.args.get('campous')
    type = request.args.get('type')
    url = "http://192.168.1.7:3000/editRoom"
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
    url = "http://192.168.1.7:3000/addCourseToDepartment?"
    url += "idDep=" + idDep + "&"
    url += "name=" + name + "&"
    url += "number=" + number + "&"
    url += "numberOfHour=" + numberOfHour + "&"
    url += "type=" + type + "&"
    url += "year=" + year + "&"
    url += "sem=" + sem



    return redirect(url)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3002)
