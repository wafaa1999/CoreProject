from pymongo import MongoClient

class dataBaseC():

    def __init__(self):

        Client = MongoClient("mongodb+srv://WD-project:wafaa12345@cluster0.v5htd.mongodb.net/test")
        self._db = Client['BackendServer']

    def get_rooms(self):
        collection = self._db.Room
        result = []
        for i in collection.find():
            result.append(i)
        return result

    def store_in_database(self, population, tableName, idDep):
        classes = population.get_schedules()[0].get_classes()
        collection = self._db.finalTable
        for i in range(len(classes)):
            time = classes[i].get_meeting_time().get_start()
            time2 = classes[i].get_meeting_time().get_end()
            if time > int(time):
                startTime = str(int(time)) + ":30"
            else:
                startTime = str(int(time)) + ":00"

            if time2 > int(time2):
                endTime = str(int(time2)) + ":30"
            else:
                endTime = str(int(time2)) + ":00"
            allDays = ""
            for j in range(len(classes[i].get_meeting_time().get_days())):
                allDays += classes[i].get_meeting_time().get_days()[j]
                if j < len(classes[i].get_meeting_time().get_days()) - 1:
                    allDays += ','
            inst = "من قسم اخر"
            room = "من قسم اخر"
            year = "لقسم اخر"
            type = "من قسم اخر"

            if not classes[i].get_course().get_from_other_department():
                inst = classes[i].get_instructor().get_name()
                room = classes[i].get_room().get_number()
                type = classes[i].get_room().get_type()
            if not classes[i].get_course().get_for_other_department():
                year = classes[i].get_course().get_year()

            row = {
                "courseNumber": classes[i].get_course().get_number(),
                "courseName": classes[i].get_course().get_name(),
                "days": allDays,
                "startHour": startTime,
                "endHour": endTime,
                "roomNumber": room,
                "instName": inst,
                "year": year,
                "tableName": tableName,
                "idDep": idDep,
                "roomType": type,
            }
            result = collection.insert_one(row)

    def add_room(self,idDep, number, type, campous, name):
        flag = self.check_room(number)
        if flag == 'False':
            collection = self._db.Room
            row = {
                "type": type,
                "number": number,
                "idDepartment": idDep,
                "campous": campous,
                "name": name
            }
            result = collection.insert_one(row)

    def add_inst_to_dep(self, idDep, name):
        collection = self._db.Inst
        row = {
            "idDepartment": idDep,
            "name": name
        }
        result = collection.insert_one(row)

    def get_istn(self):
        collection = self._db.Inst
        result = []
        for i in collection.find():
            result.append(i)
        return result



    def update_data_for_room(self, idDep, number, campous, type, name):
        flag = False
        collection = self._db["Room"]
        for i in collection.find():
            if number == i['number'] and idDep == i['idDepartment']:
                flag = True
                doc = collection.find_one_and_update(
                    {"number": number},
                    {"$set":
                         {"campous": campous,
                          "type": type,
                          "name": name}
                     }, upsert=True
                )


    def check_room(self, number):
        collection = self._db.Room
        result = []
        for i in collection.find():
            if i['number'] == number:
                return 'True'
        return 'False'

    def add_course_to_dep(self, idDep, name, number, numberOfHour, type, year, sem, flag,toDepartments, specialty):
        response = []
        flag1 = True
        if flag == '0':
            flagFrom = 'false'
            flagTo = 'false'
        elif flag == '1':
            flagFrom = 'true'
            flagTo = 'false'
        else:
            flagFrom = 'false'
            flagTo = 'true'

        result = self.get_course_of_dep(idDep)
        for i in range(len(result)):
            if result[i]['number'] == number and idDep == result[i]['idDepartment']:
                flag1 = False
        if flag1:
            collection = self._db.Course
            row = {
                "name": name,
                "type": type,
                "number": number,
                "courseHours": numberOfHour,
                "year": year,
                "idDepartment": idDep,
                "semester": sem,
                "toDepartments": toDepartments,
                "flagFrom": flagFrom,
                "flagTo": flagTo,
                "specialty":specialty,

            }

            result = collection.insert_one(row)
            response.append("1")

        else:
            response.append("0")

        return response


    def delete_room_from_dep(self, idDep, numberr):
        flag = False
        collection = self._db["Room"]
        for i in collection.find():
            if numberr == i['number'] and idDep == i['idDepartment']:
                reselt = collection.delete_one({"number": numberr})


    def save_to_draft(self, tableName, depId, courseIns, courseName, flag, timeSlot, roomType, date):
        collection = self._db.Course
        collection2 = self._db.SavedMaterial
        fromOtherDep = "false"
        toOtherDep = "false"
        if flag =='1':
            fromOtherDep = "true"
        elif flag == '2':
            toOtherDep = "true"

        result = []
        for i in collection.find():
            result.append(i)
        for j in range(len(result)):
            if result[j]['name'] == courseName:

                row = {
                    "tableName": tableName,
                    "depId": depId,
                    "courseIns": courseIns,
                    "courseName": courseName,
                    "year": result[j]['year'],
                    "semester": result[j]['semester'],
                    "fromOtherDep": fromOtherDep,
                    "toOtherDep": toOtherDep,
                    "timeSolt": timeSlot,
                    "duration": result[j]['courseHours'],
                    "roomType": roomType,
                    "date": date,
                    "courseNumber": result[j]['number'],
                    "specialty": result[j]['specialty'],
                    "orignaldep":result[j]['idDepartment'],

                }

                result = collection2.insert_one(row)
                return 'True'
        return 'False'


    def delete_from_draft(self, tableName, depId, courseIns, courseName, flag, timeSlot, roomType, date):
        collection2 = self._db.SavedMaterial
        fromOtherDep = "false"
        toOtherDep = "false"
        if flag == '1':
            fromOtherDep = "true"
        elif flag == '2':
            toOtherDep = "true"

        # for i in collection2.find():
        #     print(i['courseIns'])
        #     if tableName == i['tableName'] and depId == i['depId'] and courseIns == i['courseIns'] \
        #             and courseName == i['courseName'] and timeSlot == i['timeSolt'] and roomType == i['roomType'] and date == i['date']\
        #             and fromOtherDep == i['fromOtherDep'] and toOtherDep == i['toOtherDep']:
        reselt = collection2.delete_one({"tableName": tableName,
                                                 "depId": depId,
                                                 "courseIns": courseIns,
                                                 "courseName": courseName,
                                                 "timeSolt": timeSlot,
                                                 "roomType": roomType,
                                                 "date": date,
                                                 "toOtherDep": toOtherDep,
                                                 "fromOtherDep": fromOtherDep
                                                 })
        print(reselt)
        return 'True'




    def check_dep(self, idDep):
        collection = self._db.FristTime
        result = []
        for i in collection.find():
            if i['idDep'] == idDep:
                return 'True'  # موجوده من قبل
        row = {
            "idDep": idDep,
            "flag": 'True',
        }

        result = collection.insert_one(row)
        return 'False'

    def add_Inst_to_dep(self, idDep, name):
        collection = self._db.Inst
        row = {
            "name": name,
            "idDepartment": idDep,
        }
        result = collection.insert_one(row)

    def get_course_of_dep(self, idDep):
        course = self._db.Course
        result = []
        for i in course.find():
            result.append(i)
        return result

    def get_course_from_draft(self, idDep ,tableName):
        response = []
        course = self._db.SavedMaterial
        result = []
        for i in course.find():
            if i['depId'] == idDep and i['tableName'] == tableName:
               result.append(i)

        for i in range(len(result)):

            row = dict(
                tableName=result[i]['tableName'],
                depId=result[i]['depId'],
                courseIns=result[i]['courseIns'],
                courseName=result[i]['courseName'],
                year=result[i]['year'],
                semester=result[i]['semester'],
                fromOtherDep=result[i]['fromOtherDep'],
                toOtherDep=result[i]['toOtherDep'],
                timeSolt=result[i]['timeSolt'],
                roomType=result[i]['roomType'],
                courseNumber=result[i]['courseNumber'],
                duration=result[i]['duration'],
                specialty=result[i]['specialty'],
                orignaldep=result[i]['orignaldep'],

            )
            response.append(row)

        return response


    def add_table(self, idDep, name, year, semester, status):
        response = []
        flag = False
        collection = self._db.tables
        result = []
        for i in collection.find():
            if i['idDep'] == idDep and i['name'] == name:
              flag = True
        if not flag:
            row = {
                "name": name,
                "idDep": idDep,
                "year": year,
                "semester": semester,
                "status": status,

            }
            result = collection.insert_one(row)
            row = {
                "flag": 'true',}
        else:
            row = {
                "flag": 'false', }

        response.append(row)
        return  response

    def delete_inst_from_dep(self, idDep, name):
       response = []
       collection = self._db.Inst


       result = collection.delete_one({"idDepartment": idDep,
                               "name": name })
       row = {
            "flag": 'true', }
       response.append(row)
       return response


    def delete_table(self, idDep, name):
        response = []
        flag = False
        collection = self._db.tables

        collection.delete_one({"idDep": idDep,
                                "name": name
                                })
        row = {
            "flag": 'true', }
        response.append(row)
        return response




    def get_tables_table(self, idDep):
        response = []
        flag = False
        collection = self._db.tables
        result = []
        for i in collection.find():
            if i['idDep'] == idDep:
                result.append(i)

        for i in range(len(result)):
            row = {
                "name": result[i]['name'],
                "idDep": result[i]['idDep'],
                "year": result[i]['year'],
                "semester": result[i]['semester'],
                "status": result[i]['status'],

            }
            response.append(row)

        return response

#     def updatcourse(self):
#         collection = self._db["SavedMaterial"]
#         collection.update_many({}, {"$set": {"specialty": "هندسة حاسوب"}}, upsert=False, array_filters=None)
#
#
# d = dataBaseC().updatcourse()
#
#
