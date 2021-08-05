from DataBaseConnection import dataBaseC
from DataClass import Data
from Solve import Solve


class MainSolving:
    def solveMain(self, idDep, tableName, softFlag):
        ROOMS = []
        INSTRUCTORS = []
        data = dataBaseC()
        # Rooms
        result = data.get_rooms()
        for i in range(len(result)):
            if result[i]['idDepartment'] == idDep:
               ROOMS.append([result[i]['number'], result[i]['name']])

        #INSTRUCTORS
        result = data.get_istn()
        for i in range(len(result)):
            if result[i]['idDepartment'] == idDep:
               INSTRUCTORS.append([str(result[i]['_id']), result[i]['name'], False])





        MEETING_TIMES_1 = [["MT1", 8, 9, ["Sunday", "Tuesday", "Thursday"]],
                           ["MT2", 9, 10, ["Sunday", "Tuesday", "Thursday"]],
                           ["MT3", 10, 11, ["Sunday", "Tuesday", "Thursday"]],
                           ["MT4", 11, 12, ["Sunday", "Tuesday", "Thursday"]],
                           ["MT5", 13, 14, ["Sunday", "Tuesday", "Thursday"]],
                           ["MT6", 14, 15, ["Sunday", "Tuesday", "Thursday"]],
                           ["MT7", 8, 9.5, ["Monday", "Wednesday"]],
                           ["MT8", 9.5, 11, ["Monday", "Wednesday"]],
                           ["MT9", 11, 12.5, ["Monday", "Wednesday"]],
                           ["MT10", 12.5, 14, ["Monday", "Wednesday"]],
                           ["MT11", 14, 15.5, ["Monday", "Wednesday"]],
                           ]

        # MEETING_TIMES_1 = [["MT1", 8, 9.5, ["Saturday", "Tuesday"]],
        #                    ["MT2", 9.5, 11, ["Saturday", "Tuesday"]],
        #                    ["MT3", 11, 12.5, ["Saturday", "Tuesday"]],
        #                    ["MT4", 12.5, 14, ["Saturday", "Tuesday"]],
        #                    ["MT5", 14, 15.5, ["Saturday", "Tuesday"]],
        #
        #                    ["MT6", 8, 9.5, ["Sunday", "Wednesday"]],
        #                    ["MT7", 9.5, 11, ["Sunday", "Wednesday"]],
        #                    ["MT8", 11, 12.5, ["Sunday", "Wednesday"]],
        #                    ["MT9", 12.5, 14, ["Sunday", "Wednesday"]],
        #                    ["MT10", 14, 15.5, ["Sunday", "Wednesday"]],
        #
        #                    ["MT11", 8, 9.5, ["Monday", "Thursday"]],
        #                    ["MT12", 9.5, 11, ["Monday", "Thursday"]],
        #                    ["MT13", 11, 12.5, ["Monday", "Thursday"]],
        #                    ["MT14", 12.5, 14, ["Monday", "Thursday"]],
        #                    ["MT15", 14, 15.5, ["Monday", "Thursday"]],
        #                    ]

        MEETING_TIMES_2 = [["MT16", 8, 11, ["Sunday"]], ["MT17", 11, 14, ["Sunday"]],
                           ["MT18", 8, 11, ["Monday"]], ["MT19", 11, 14, ["Monday"]],
                           ["MT20", 8, 11, ["Tuesday"]], ["MT21", 11, 14, ["Tuesday"]],
                           ["MT22", 8, 11, ["Wednesday"]], ["MT23", 11, 14, ["Wednesday"]],
                           ["MT24", 8, 11, ["Thursday"]], ["MT25", 11, 14, ["Thursday"]],
                           ]

        MEETING_TIMES_LABS = [["MT26", 14, 17, ["Sunday"]],
                              ["MT27", 14, 17, ["Monday"]],
                              ["MT28", 14, 17, ["Tuesday"]],
                              ["MT29", 14, 17, ["Wednesday"]],
                              ["MT30", 14, 17, ["Thursday"]]]

        MEETING_TIMES_3 = [["MT27", 8, 9, ["Sunday", "Tuesday"]],
                           ["MT28", 9, 10, ["Sunday", "Tuesday"]]]

        # INSTRUCTORS = [["I1", "اسماء عفيفي", False],
        #                ["I2", "اشرف عرموش", True],
        #                ["I3", "انس طعمة", False],
        #                ["I4", "رائد القاضي", False],
        #                ["I6", "سفيان سمارة", False],
        #                ["I7", "سليمان ابو خرمة", False],
        #                ["I8", "عبد الله راشد", False],
        #                ["I9", "علاء الدين المصري", False],
        #                ["I10", "عماد النتشة", False],
        #                ["I11", "لؤي ملحيس", False],
        #                ["I12", "منار قمحية", True],
        #                ["I13", "منى الضميدي", True],
        #                ["I14", "مهند الجابي", True],
        #                ["I15", "هنال ابو زنط", True],
        #                ["I16", "هيا سماعنة", False]
        #                ]

        # instructor_ID , days , start time ,end time , is_wanted , weight
        SOFT_CONSTRAINTS = [["I1", ["Sunday", "Tuesday"], 8, 9, False, 0.5],
                            ["I1", ["Sunday", "Tuesday", "Thursday"], 10, 11, False, 1]
            , ["I3", ["Sunday", "Tuesday"], 8, 9, False, 0.5]]

        toSolve = Solve(ROOMS, MEETING_TIMES_1, MEETING_TIMES_LABS, MEETING_TIMES_3, INSTRUCTORS, MEETING_TIMES_2,
                        SOFT_CONSTRAINTS,idDep, tableName, softFlag)
        toSolve.solve()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



# s = MainSolving()
# s.solveMain('60ddc9735b4d43f8eaaabf83', 'firstSem', 'false')
