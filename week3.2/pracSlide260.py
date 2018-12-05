# homework อ่านไฟลแล้วแยก ว่าคอมเมนต์ไหนสามารถโชวได้ แสดง bad comment ว่ากี่เปอเซนของทั้งหมด
#Prepare two file  goo.gl/DnRZwX
#Slide 260-263

import os.path
from pracLibrary import checkWord

def readFile(filename): #.readlines()
    with open (filename,'r',encoding='UTF-8') as f :
        data = f.readlines()
        return data

def workingWithFile(filename,m,data):
    with open(filename,mode=m,encoding='UTF-8') as f :
        for i in range(len(data)):
            f.write('{0}\n'.format(data[i]))


if __name__ == '__main__':
    commentfile = 'myFile/practice-comment.txt'
    rudewordfile = 'myFile/rude_word.txt'
    filecanshow = 'myFile/canshow.txt'
    filecannotshow = 'myFile/cannotshow.txt'
    if os.path.exists(commentfile) and os.path.exists(rudewordfile):
        comment = readFile(commentfile)
        rudeword = readFile(rudewordfile)
    else:
        print('"{0} or {1}" is missing'.format(commentfile,rudewordfile))

    canshowlist,cannotshowlist = checkWord(comment,rudeword)

    if os.path.exists(filecanshow):
        mode = 'w'
    else:
        mode = 'x'
    workingWithFile(filecanshow, mode, canshowlist)

    if os.path.exists(filecannotshow):
        mode = 'w'
    else:
        mode = 'x'
    workingWithFile(filecannotshow, mode, cannotshowlist)