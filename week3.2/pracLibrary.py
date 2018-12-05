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

def setConfig(config):
    splitdecimal = config[0].split('=')
    decimal = splitdecimal[1].replace('\n', '')
    if (decimal == '') or (int(decimal) < 0):
        decimal = 0

    splitcomma = config[1].split('=')
    commacheck = splitcomma[1].replace('\n', '')
    if (commacheck == 'yes'):
        comma = ','
    else:
        comma = ''

    splitline = config[2].split('=')
    line = splitline[1].replace('\n', '')

    splitunit = config[3].split('=')
    unit = splitunit[1].replace('\n', '')

    return decimal,comma,line,unit

def checkWord(comment,rudeword):
    commentcount = 0
    badcomment = 0
    canshowlist, cannotshowlist = [],[]
    for i in range(len(comment)):
        commentcount+=1
        canshow = True
        lcomment = comment[i].lower().replace('\n','')
        scomment = lcomment.split(' ')
        for x in scomment:
            for z in rudeword:
                lrudeword = z.lower().replace('\n','')
                if (x==lrudeword):
                    canshow=False
        if(canshow):
            canshowlist.append(lcomment)
        else:
            cannotshowlist.append(lcomment)
            badcomment += 1
    badfeedback = badcomment/commentcount*100
    print('Bad Feedback = {:.2f}%'.format(badfeedback))
    return canshowlist,cannotshowlist
