# import statements
import nao_nocv_2_1 as nao


asr = ALProxy("ALSpeechRecognition", IP, 9559)

asr.subscribe("MyModule")
asr.unsubscribe("MyModule")
