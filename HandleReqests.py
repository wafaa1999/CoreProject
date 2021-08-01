from flask import Flask, jsonify, redirect, request
from flask_cors import CORS
from reqest import req

from DataBaseConnection import dataBaseC

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


@app.route("/firstTime", methods=['GET'])
def firstTime():
    response = []
    idUser = request.args.get('idUser')
    password = request.args.get('password')
    req1 = req()
    re = req1.get_dep(idUser,password)
    row = dict(
        stat=re
    )
    response.append(row)
    return jsonify({'response': response})


@app.route("/checkAndSendEmail", methods=['GET'])
def redirect_checkAndSendEmail():
    email = request.args.get('email')
    url = "https://virtual-grad.herokuapp.com/checkAndSendEmail"
    # url = "http://127.0.0.1:5000/checkAndSendEmail"
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
    # url = "https://virtual-grad.herokuapp.com/getRoomsofDep"
    url = "http://127.0.0.1:5000/getRoomsofDep"
    url += "?idDep=" + idDep
    return redirect(url)


@app.route("/editRoom", methods=['GET'])
def redirect_editRoom():
    idDep = request.args.get('idDep')
    number = request.args.get('number')
    campous = request.args.get('campous')
    type = request.args.get('type')
    name = request.args.get('name')
    data4 = dataBaseC()
    data4.update_data_for_room( idDep, number, campous, type, name)
    url = "https://virtual-grad.herokuapp.com/editRoom"
    url += "?idDep=" + idDep
    url += "&number=" + number
    url += "&campous=" + campous
    url += "&type=" + type
    url += "&name=" + name
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
    flag = request.args.get('flag')
    toDepartments = request.args.get('toDepartments')
    data2 = dataBaseC()
    data2.add_course_to_dep(idDep, name, number, numberOfHour, type, year, sem, flag,toDepartments)
    url = "https://virtual-grad.herokuapp.com/addCourseToDepartment?"
    url += "idDep=" + idDep + "&"
    url += "name=" + name + "&"
    url += "number=" + number + "&"
    url += "numberOfHour=" + numberOfHour + "&"
    url += "type=" + type + "&"
    url += "year=" + year + "&"
    url += "sem=" + sem + "&"
    url += "flag=" + flag + "&"
    url += "toDepartments=" + toDepartments
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
    name = request.args.get('name')
    data1 = dataBaseC()
    data1.add_room(idDep, number, type, campous, name)
    url = "https://virtual-grad.herokuapp.com/addRoomToDepartment"
    url += "?idDep=" + idDep
    url += "&number=" + number
    url += "&type=" + type
    url += "&campous=" + campous
    url += "&name=" + name
    return redirect(url)



@app.route("/saveMatOfDraft", methods=['GET'])
def saveMatOfDraft():
    response = []
    tableName = request.args.get('tableName')
    depId = request.args.get('depId')
    courseIns = request.args.get('courseIns')
    courseName = request.args.get('courseName')
    flag = request.args.get('flag')
    timeSlot = request.args.get('timeSlot')
    roomType = request.args.get('roomType')
    date = request.args.get('date')
    data1 = dataBaseC()
    result =data1.save_to_draft(tableName, depId, courseIns, courseName, flag, timeSlot, roomType, date)
    row = dict(
        stat=result
    )
    response.append(row)
    return jsonify({'response': response})


@app.route("/getAllIsn", methods=['GET'])
def getAllIsn():
    idDep = request.args.get('idDep')
    url = "https://virtual-grad.herokuapp.com/getAllIsn"
    url += "?idDep=" + idDep
    return redirect(url)


@app.route("/deleteRoomFromDep", methods=['GET'])
def deleteRoomFromDep():
    idDep = request.args.get('idDep')
    number = request.args.get('number')
    data3 = dataBaseC()
    data3.delete_room_from_dep(idDep, number)
    url = "https://virtual-grad.herokuapp.com/deleteRoomFromDep"
    url += "?idDep=" + idDep
    url += "&number=" + number
    return redirect(url)

@app.route("/deleteFromSaveMatOfDraft", methods=['GET'])
def deleteFromSaveMatOfDraft():
    response = []
    tableName = request.args.get('tableName')
    depId = request.args.get('depId')
    courseIns = request.args.get('courseIns')
    courseName = request.args.get('courseName')
    flag = request.args.get('flag')
    timeSlot = request.args.get('timeSlot')
    roomType = request.args.get('roomType')
    date = request.args.get('date')
    data1 = dataBaseC()
    result =data1.delete_from_draft(tableName, depId, courseIns, courseName, flag, timeSlot, roomType,date)
    row = dict(
        stat=result
    )
    response.append(row)
    return jsonify({'response': response})


@app.route("/getFromDraft", methods=['GET'])
def getFromDraft():
    idDep = request.args.get('idDep')
    db = dataBaseC()
    response = db.get_course_from_draft(idDep)
    return jsonify({'response': response})

@app.route("/getAllDep", methods=['GET'])
def getAllDep():
    url = "https://virtual-grad.herokuapp.com/getAllDep"
    return redirect(url)

# @app.route("/testingPost", methods=['POST'])
# def testu():
#     list = request
#     print("WAfaa")
#     return "true"

@app.route("/getMatOfSpeDep", methods=['GET'])
def getMatOfSpeDep():
    idDep = request.args.get('idDep')
    id = request.args.get('id')
    url = "https://virtual-grad.herokuapp.com/getMatOfSpeDep"
    url += '?idDep=' + idDep
    url += '&id=' + id
    return redirect(url)

@app.route("/addTable", methods=['GET'])
def addTable():
    idDep = request.args.get('idDep')
    name = request.args.get('name')
    year = request.args.get('year')
    semester = request.args.get('semester')
    status = request.args.get('status')
    response = dataBaseC().add_table(idDep, name, year, semester, status)
    return jsonify({'response': response})


@app.route("/deleteTable", methods=['GET'])
def deleteTable():
    idDep = request.args.get('idDep')
    name = request.args.get('name')
    response = dataBaseC().delete_table(idDep, name)
    return jsonify({'response': response})

@app.route("/getTables", methods=['GET'])
def getTables():
    idDep = request.args.get('idDep')
    response = dataBaseC().get_tables_table(idDep)
    return jsonify({'response': response})

@app.route("/wafaa", methods=['POST'])
def wafaa():
    response = []
    name  = request.form['name']
    num = request.form['num']
    print(name)
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3015)