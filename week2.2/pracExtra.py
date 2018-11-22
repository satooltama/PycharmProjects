from pracLibrary import _94main,line

score = []

while True:
   Name = input ('Enter Name : ')
   Mid = int(input('Enter Midterm : '))
   Fin = int(input('Enter Final   : '))
   Hom = int(input('Enter Homework : '))
   eachScore = (Name,Mid,Fin,Hom)
   score.append(eachScore)
   line()
   Cont = input ('Continue Y/N : ')
   line()
   if Cont.upper() == 'Y':
       break

line()
_94main(tuple(score))
