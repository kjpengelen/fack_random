import naoqi
from naoqi import ALProxy
import nao_nocv_2_1 as nao
import time
# import math

IP='192.168.0.117'
nao.InitProxy(IP)
asr = ALProxy("ALSpeechRecognition", IP, 9559)

def Greeting():
    #nao.Say("Hello, my name is Bender. There appears to be an emergency.")
    #nao.Say("It's my task to help the patients find the emergency exits.")
    nao.Say("Test one")

def OfferHelp():
    i = 0
    j = 0

    nao.Say("Will you follow me?")

    while i == 0:
        time.sleep(1)
        asr.subscribe("MyModule")
        time.sleep(3)
        result = nao.DetectSpeech()

        if len(result) > 0:
            print result
            if result[0] == myWordList[0]:
                print "Registerd response: ", myWorldList[0]
                nao.Say("Hey, hoe, let's go.")
                time.sleep(1)
                nao.Say("Follow me")
                i = 1
                break
            elif result[0] == myWordList[1] and j == 0:
                print "Registered response: ", myWorldList[1]
                nao.Say("Are you sure? You're not safe here!")
                nao.Say("Do you want me to help you?")
                j = 1
                break
            elif result[0] == myWorldList[1] and j == 1:
                print "Registered response: ", myWorldList[1]
                nao.Say("Okay, but don't come crying to me if you get hurt")
                i = 1
            else:
                nao.EyeLED([0, 255, 0])
                nao.EyeLED([0, 0, 255])
                nao.Say("I'm sorry, I didn't understand you.")
                nao.Say("Did you say yes or no?")

def LeadTheWay():
    nao.Say("Step three, Lead The Way")

def workingConvo():
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
          
