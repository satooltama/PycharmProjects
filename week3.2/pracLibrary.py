from operator import itemgetter
def stat_point_goalD(value):

    for i in range(len(value)):
        point = (value[i]['W']*3) + (value[i]['D'])
        value[i]['Point'] = point

    for i in range(len(value)):
        gd = (value[i]['GF']-value[i]['GA'])
        value[i]['GD'] = gd

    for i in range(len(value)):
        print('{0:2} {1:30} Pts:{2:3} GD:{3:4}'.format(value[i]['Pos'],
                                                       value[i]['Team'],
                                                       value[i]['Point'],
                                                       value[i]['GD']))

def stat_percentages(value):
    for i in range(len(value)):
        match = value[i]['W']+value[i]['D']+value[i]['L']
        winP = value[i]['W'] / match *100
        drawP = value[i]['D'] / match *100
        loseP =value[i]['L'] / match *100
        value[i]['Win%'] = winP
        value[i]['Draw%'] = drawP
        value[i]['Lose%'] = loseP

    value = sorted(value,key=itemgetter('Team'))

    for i in range(len(value)):
        print('{0:2} {1:30} WIN[{2:3.02f}%] Draw[{3:4.02f}%] Lose[{4:4.02f}%]'
            .format(i+1,value[i]['Team'],value[i]['Win%'],
                    value[i]['Draw%'],value[i]['Lose%']))
