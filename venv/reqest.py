import requests
from DataBaseConnection import dataBaseC

class req:
    def __init__(self):
        self._data5 = dataBaseC()

    def get_dep(self,idUser,password):
       URL = "http://127.0.0.1:5000/getDep"
       username = idUser
       passs= password
       PARAMS = {'username': idUser,
                 'passs':password}
       r = requests.get(url=URL, params=PARAMS)
       data = r.json()
       if not data['response'][0]['idDep'] == 'None':
           self._data5.
           # بدي اعمل تشيك اذا اول مره ولا لا
           # تلات اضافه ع الداتا بيس
          result1 = self.get_room(data['response'][0]['idDep'])
          result2 = self.get_mat(data['response'][0]['idDep'])
          result3 = self.get_inst(data['response'][0]['idDep'])


          
    def get_room(self,idDepu):
        result = []
        URL = "http://127.0.0.1:5000/getRoomsofDep"
        idDep = idDepu
        PARAMS = {'idDep': idDepu}
        r = requests.get(url=URL, params=PARAMS)
        data = r.json()
        for i in range(len(data['response'])):
            result.append([data['response'][i]['number'],data['response'][i]['type'],
                           idDepu,data['response'][i]['campous']])
        return result

    def get_mat(self, idDepu):
        result = []
        URL = "http://127.0.0.1:5000/getAllMaterialsOfDepartment"
        idDep = idDepu
        PARAMS = {'idDep': idDepu}
        r = requests.get(url=URL, params=PARAMS)
        data = r.json()
        for i in range(len(data['response'])):
            result.append([data['response'][i]['name'], data['response'][i]['number'],
                           data['response'][i]['year'], data['response'][i]['type'],
                           data['response'][i]['courseHours'], data['response'][i]['idDepartment'],
                           data['response'][i]['semester'],data['response'][i]['toDepartments']])

        return result

    def get_inst(self,idDepu):
        result = []
        URL = "http://127.0.0.1:5000/getAllIsn"
        idDep = idDepu
        PARAMS = {'idDep': idDepu}
        r = requests.get(url=URL, params=PARAMS)
        data = r.json()
        for i in range(len(data['response'])):
            result.append([data['response'][i]['name'],data['response'][i]['idDepartment']])
        return result

            


re =req().get_dep('123','123')