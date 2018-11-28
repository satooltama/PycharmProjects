from pracLibrary import line

flowers = ["Sun flower","Ivy","Jusmine","Lily"]

SortedFlower = sorted(flowers)

for i in range(len(SortedFlower)):
    print ("{0:3}. {1:1}".format(i+1,SortedFlower[i]))

line()
