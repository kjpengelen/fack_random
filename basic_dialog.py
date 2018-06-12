import naoqi
from naoqi import ALProxy
import nao_nocv_2_1 as nao
import time
import math

IP='192.168.0.115'
nao.InitProxy(IP)
asr = ALProxy("ALSpeechRecognition", IP, 9559)

def screen1():
    myWordList = ("Hello", "Fine", "good","Yes","No","Thanks")
    myLanguage="English"
    nao.InitSpeech(myWordList, myLanguage)

    nao.Say("How are you doing today?")

    for i in range (0,10):
        time.sleep(1)
        asr.subscribe("MyModule")
        time.sleep(3)
        result = nao.DetectSpeech()
 
        if len(result) > 0:
            print result
            if result[0] == myWordList[1]:
                print "myworldlist", myWordList[1]
                nao.Say("Great to hear")
                break
            if result[0] == myWordList[2]:
                print "myworldlist", myWordList[2]
                nao.Say("Great to hear")
                break
        else:
            nao.EyeLED([0, 255, 0])
            nao.EyeLED([0, 0, 255])
            print "I don't understand"

    asr.unsubscribe("MyModule")
          
