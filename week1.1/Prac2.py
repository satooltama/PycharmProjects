weight = input('Weight(kg.) :')
height = input('Height(cm.) :')

def calBMI(weight,height):
    heightmeter = float(height) / 100
    heightmeterforbmi = heightmeter * 2
    bmi = int(weight) / heightmeterforbmi
    return bmi

print('Your BMI = {0:.2f}'.format(calBMI(weight,height)))
