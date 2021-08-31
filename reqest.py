import requests
from DataBaseConnection import dataBaseC


class req:
    def __init__(self):
        self._data5 = dataBaseC()

    def get_dep(self, idUser, password):
        URL = "https://virtual-grad.herokuapp.com/getDep"
        username = idUser
        passs = password
        PARAMS = {'username': idUser,
                  'passs': password}
        r = requests.get(url=URL, params=PARAMS)
        data = r.json()
        if not data['response'][0]['idDep'] == 'None':
            res = self._data5.check_dep(data['response'][0]['idDep'])
            if res == 'False':
                result1 = self.get_room(data['response'][0]['idDep'])
                result2 = self.get_mat(data['response'][0]['idDep'])
                result3 = self.get_inst(data['response'][0]['idDep'])
                for i in range(len(result1)):
                    self._data5.add_room(result1[i][2], result1[i][0], result1[i][1], result1[i][3])
                for j in range(len(result2)):
                    self._data5.add_course_to_dep(result2[j][5], result2[j][0], result2[j][1], result2[j][4],
                                                  result2[j][3], result2[j][2], result2[j][6])
                for k in range(len(result3)):
                    self._data5.add_inst_to_dep(self, result3[k][1], result3[k][0], '', '')
                return 'True'
        return 'False'

    def get_room(self, idDepu):
        result = []
        URL = "https://virtual-grad.herokuapp.com/getRoomsofDep"
        idDep = idDepu
        PARAMS = {'idDep': idDepu}
        r = requests.get(url=URL, params=PARAMS)
        data = r.json()
        for i in range(len(data['response'])):
            result.append([data['response'][i]['number'], data['response'][i]['type'],
                           idDepu, data['response'][i]['campous'],data['response'][i]['name']])
        return result

    def get_mat(self, idDepu):
        result = []
        URL = "https://virtual-grad.herokuapp.com/getAllMaterialsOfDepartment"
        idDep = idDepu
        PARAMS = {'idDep': idDepu}
        r = requests.get(url=URL, params=PARAMS)
        data = r.json()
        for i in range(len(data['response'])):
            result.append([data['response'][i]['name'], data['response'][i]['number'],
                           data['response'][i]['year'], data['response'][i]['type'],
                           data['response'][i]['courseHours'], data['response'][i]['idDepartment'],
                           data['response'][i]['semester'], data['response'][i]['toDepartments']])

        return result

    def get_inst(self, idDepu):
        result = []
        URL = "https://virtual-grad.herokuapp.com/getAllIsn"
        idDep = idDepu
        PARAMS = {'idDep': idDepu}
        r = requests.get(url=URL, params=PARAMS)
        data = r.json()
        for i in range(len(data['response'])):
            result.append([data['response'][i]['name'], data['response'][i]['idDepartment']])

        return result