import naoqi
from naoqi import ALProxy
import nao_nocv_2_1 as nao
import time
import math

IP='192.168.0.117'
nao.InitProxy(IP)
asr = ALProxy("ALSpeechRecognition", IP, 9559)

def screen1():
    myWordList = ()
    myLanguage="English"
    nao.InitSpeech(myWordList, myLanguage)


    asr.subscribe("MyModule")

    asr.unsubscribe("MyModule")
          
