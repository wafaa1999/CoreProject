from DataClass import Data
from Solve import Solve


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.





if __name__ == '__main__':
    print_hi('PyCharm')
    ROOMS = [["114070", "A"], ["114040", "A"], ["112020", "A"],  ["111190", "A"],
             ["111181", "A"],
             ["11B1160", "B"],["11B1140","F"], ["11B1150", "D"], ["11B1141", "C"],
             ["114080","G"],["113080", "E"]]

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

    INSTRUCTORS = [["I1", "اسماء عفيفي",False],
                   ["I2", "اشرف عرموش",True],
                   ["I3", "انس طعمة",False],
                   ["I4", "رائد القاضي",False],
                   ["I6", "سفيان سمارة",False],
                   ["I7", "سليمان ابو خرمة",False],
                   ["I8", "عبد الله راشد",False],
                   ["I9", "علاء الدين المصري",False],
                   ["I10", "عماد النتشة",False],
                   ["I11", "لؤي ملحيس",False],
                   ["I12", "منار قمحية",True],
                   ["I13", "منى الضميدي",True],
                   ["I14", "مهند الجابي",True],
                   ["I15", "هنال ابو زنط",True],
                   ["I16", "هيا سماعنة",False]
                   ]


    # instructor_ID , days , start time ,end time , is_wanted , weight
    SOFT_CONSTRAINTS = [["I1", ["Sunday", "Tuesday"], 8, 9, False, 0.5],
                        ["I1", ["Sunday", "Tuesday", "Thursday"], 10, 11, False, 1]
        , ["I3", ["Sunday", "Tuesday"], 8, 9, False, 0.5]]

    toSolve = Solve(ROOMS,MEETING_TIMES_1,MEETING_TIMES_LABS,MEETING_TIMES_3,INSTRUCTORS,MEETING_TIMES_2, SOFT_CONSTRAINTS)
    toSolve.solve()





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
