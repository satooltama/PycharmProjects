# 2 function
from operator import itemgetter
def stat_point_goalD(value):

    for i in range(len(value)):
        point = (value[i]['Result']['W']*3) + (value[i]['Result']['D'])
        value[i]['Point'] = point

    for i in range(len(value)):
        gd = (value[i]['Goal']['GF']-value[i]['Goal']['GA'])
        value[i]['GD'] = gd

    for i in range(len(value)):
        print('{0:2} {1:30} Pts:{2:3} GD:{3:4}'.format(value[i]['Pos'],
                                                       value[i]['Team'],
                                                       value[i]['Point'],
                                                       value[i]['GD']))

def stat_percentages(value):
    for i in range(len(value)):
        match = value[i]['Result']['W']+value[i]['Result']['D']+value[i]['Result']['L']
        winP = value[i]['Result']['W'] / match *100
        drawP = value[i]['Result']['D'] / match *100
        loseP =value[i]['Result']['L'] / match *100
        value[i]['Win%'] = winP
        value[i]['Draw%'] = drawP
        value[i]['Lose%'] = loseP

    value = sorted(value,key=itemgetter('Team'))

    for i in range(len(value)):
        print('{0:2} {1:30} WIN[{2:3.02f}%] Draw[{3:4.02f}%] Lose[{4:4.02f}%]'
            .format(i,value[i]['Team'],value[i]['Win%'],
                    value[i]['Draw%'],value[i]['Lose%']))


premier_league_2017_2018 = [{"Pos":1,"Team":"Manchester City (C)",
                             "Result":{"W":32,"D":4,"L":2},"Goal":{"GF":106,"GA":27}},
                            {"Pos":2,"Team":"Manchester United",
                             "Result":{"W":25,"D":6,"L":7},"Goal":{"GF":68,"GA":28}},
                            {"Pos":3,"Team":"Tottenham Hotspur",
                             "Result":{"W":23,"D":8,"L":7},"Goal":{"GF":74,"GA":36}},
                            {"Pos":4,"Team":"Liverpool",
                             "Result":{"W":21,"D":12,"L":5},"Goal":{"GF":84,"GA":38}},
                            {"Pos":5,"Team":"Chelsea",
                             "Result":{"W": 21,"D":7,"L":10},"Goal":{"GF":62,"GA":38}},
                            {"Pos":6,"Team":"Arsenal",
                             "Result":{"W":19,"D":6,"L":13},"Goal":{"GF":74,"GA":51}},
                            {"Pos":7,"Team":"Burnley",
                             "Result":{"W":14,"D":12,"L":12},"Goal": {"GF":36,"GA":39}},
                            {"Pos":8,"Team":"Everton",
                             "Result":{"W":13,"D":10,"L":15},"Goal":{"GF":44,"GA":58}},
                            {"Pos":9,"Team":"Leicester City",
                             "Result":{"W":12,"D":11,"L":15},"Goal":{"GF":56,"GA":60}},
                            {"Pos":10,"Team":"Newcastle United",
                             "Result":{"W":12,"D":8,"L":18},"Goal":{"GF":39,"GA":47}},
                            {"Pos":11,"Team":"Crystal Palace",
                             "Result":{"W":11,"D":11,"L":16},"Goal":{"GF":45,"GA":55}},
                            {"Pos":12,"Team":"Bournemouth",
                             "Result":{"W":11,"D":11,"L":16},"Goal":{"GF":45,"GA":61}},
                            {"Pos":13,"Team":"West Ham United",
                             "Result":{"W":10,"D":12,"L":16},"Goal":{"GF":48,"GA":68}},
                            {"Pos":14,"Team":"Watford",
                             "Result":{"W":11,"D":8,"L":19},"Goal":{"GF":44,"GA":64}},
                            {"Pos":15,"Team":"Brighton & Hove Albion",
                             "Result":{"W":9,"D":13,"L":16},"Goal":{"GF":34,"GA":54}},
                            {"Pos":16,"Team":"Huddersfield Town",
                             "Result":{"W":9,"D":10,"L":19},"Goal":{"GF":28,"GA":58}},
                            {"Pos":17,"Team":"Southampton",
                             "Result":{"W":7,"D":15,"L":16},"Goal":{"GF":37,"GA":56}},
                            {"Pos":18,"Team":"Swansea City (R)",
                             "Result":{"W":8,"D":9,"L":21},"Goal":{"GF":28,"GA":56}},
                            {"Pos":19,"Team":"Stoke City (R)",
                             "Result":{"W":7,"D":12,"L":19},"Goal":{"GF":35,"GA":68}},
                            {"Pos":20,"Team":"West Bromwich Albion (R)",
                             "Result":{"W":6,"D":13,"L":19},"Goal":{"GF":31,"GA":56}}]
stat_point_goalD(premier_league_2017_2018)
print('-'*30)
stat_percentages(premier_league_2017_2018)
