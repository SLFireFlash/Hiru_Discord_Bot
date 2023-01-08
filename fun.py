import json
from random import randint

global uNameList
global sCount
global uName
uName = ""
sCount =[]
uNameList =[]



#imoji gen

def coolImoji():
    with open ("json/coolImoji.json",'r')as iF:
        idata =json.load(iF)
        num =str(randint(0,19))
    return idata[num]

def angryImoji():
    with open ("json/angryImoji.json",'r')as iF:
        idata =json.load(iF)
        num =str(randint(0,20))
    return idata[num]

def loveImoji():
    with open ("json/loveImoji.json",'r')as iF:
        idata =json.load(iF)
        num =str(randint(0,4))
    return idata[num]

#quortes gen
def hi():
    #gen random line
    with open ("json/hiList.json","r",encoding="utf8")as openfile:
        data =json.load(openfile)
        num = str(randint(0,13))            
        HiL =data[num]

    
    return HiL

def bye():
    with open ("json/byeList.json","r",encoding="utf8")as openfile:
        data =json.load(openfile)
        num = str(randint(0,3))            
        byeL =data[num]

    return byeL

def cmd():
    #gen random line
    with open ("json/angryList.json","r",encoding="utf8")as openfile:
        data =json.load(openfile)
        num = str(randint(0,6))            
        cmdL =data[num]

    return cmdL

def love():
    #gen random line
    with open ("json/loveList.json","r",encoding="utf8")as openfile:
        data =json.load(openfile)
        num = str(randint(0,14))            
        loveL =data[num]

    return loveL


def spamFillter():
    if not uNameList:
        uNameList.append(uName)
    else:    
        if uNameList[0] == uName:
            sCount.append("w")
            if (len(sCount)>=4):
                if (len(sCount)>=7):
                    if(len(sCount)>=9):
                        sCount.clear()
                        return 3
                    else:
                        return 2
                else:
                    return 1
        else:
            uNameList[0]=uName












    

