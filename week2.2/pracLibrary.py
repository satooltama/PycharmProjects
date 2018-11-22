def line():
    print('*'*40)

def scoresum(m,f,h):
    m = int(m)*0.3
    f = int(f)*0.5
    h = int(h)*0.2

    sum = m+f+h

    return int(sum)

def gradeScale(sum):
    if sum > 97:
        return 'A+'
    elif sum > 93:
        return 'A'
    elif sum > 90:
        return 'A-'
    elif sum > 87:
        return 'B+'
    elif sum > 83:
        return 'B'
    elif sum > 80:
        return 'B-'
    elif sum > 77:
        return 'C+'
    elif sum > 73:
        return 'C'
    elif sum > 70:
        return 'C-'
    elif sum > 67:
        return 'D+'
    elif sum > 63:
        return 'D'
    elif sum > 60:
        return 'D-'
    elif sum < 59:
        return 'F'

def _94main(score):


    for i in range(len(score)):
        scoresum(score[i][1],score[i][2],score[i][3])
        print('Name = {}'.format(score[i][0]))
        print('Score = {}'.format(scoresum(score[i][1],score[i][2],score[i][3])))
        print('Grade = {}'.format(gradeScale(scoresum(score[i][1],score[i][2],score[i][3]))))
        line()

