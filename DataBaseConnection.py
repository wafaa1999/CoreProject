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


    def add_room(self,idDep, number, type, campous):
        flag = self.check_room(number)
        if flag == 'False':
            collection = self._db.Room
            row = {
                "type": type,
                "number": number,
                "idDepartment": idDep,
                "campous": campous
            }
            result = collection.insert_one(row)

    def update_data_for_room(self, idDep, number, campous, type):
        flag = False
        collection = self._db["Room"]
        for i in collection.find():
            if number == i['number'] and idDep == i['idDepartment']:
                flag = True
                doc = collection.find_one_and_update(
                    {"number": number},
                    {"$set":
                         {"campous": campous,
                          "type": type}
                     }, upsert=True
                )


    def check_room(self, number):
        collection = self._db.Room
        result = []
        for i in collection.find():
            if i['number'] == number:
                return 'True'
        return 'False'

    def add_course_to_dep(self, idDep, name, number, numberOfHour, type, year, sem):
        collection = self._db.Course
        row = {
            "name": name,
            "type": type,
            "number": number,
            "courseHours": numberOfHour,
            "year": year,
            "idDepartment": idDep,
            "semester": sem,
            "toDepartments": idDep,
        }

        result = collection.insert_one(row)

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
        if flag ==1:
            fromOtherDep = "true"
        elif flag ==2:
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
                }

                result = collection2.insert_one(row)
                return 'True'









