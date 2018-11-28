wantedskill = {"C#" , "Python" , "Java" ,"PHP" , "SQL" , "Go"}
applicant1skill = {"VB","C","Ruby","Java","HTML"}
applicant2skill = {"C#","HTML","R","PHP","SQL","Swift","PHP"}
applicant3skill = {"Java","C++","Ruby","JavaScript","Objective-C","Go"}
applicant4skill = {"Java","Python","Go","SQL","Swift"}
applicant5skill = {"C++","C","C#","Objective-C","JavaScript","SQL"}

print((wantedskill & applicant1skill))
print((wantedskill & applicant2skill))
print((wantedskill & applicant3skill))
print((wantedskill & applicant4skill))
print((wantedskill & applicant5skill))

print('{0:1,.2f}'.format(len(wantedskill & applicant1skill) / len(wantedskill)*100))
