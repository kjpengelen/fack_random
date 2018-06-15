
import nao_nocv_2_1 as nao
import converse as conv
import behaviors as beh
import time



#function definitions
def DoStateInit():
    """Do initialiazation"""
    beh.InitRobot()
    print("1")
    return "My state A"
    
def DoStateA(mystate):
    """Execute state A"""

    if mystate=="My state A":
        conv.Greeting()
        return "My state B"
        print("2")
        pass
    elif mystate=="My state B":
        print("3")
        pass
    return "My state B"

def DoStateB():
    """Execute state B"""

    if mystate=="My state B":
        conv.OfferHelp()
        print("4")
        pass
    elif mystate=="My state C":
        print("5")
        pass
    return "My state C"

def DoStateC():
    """Execute state C"""

    if mystate=="My state C""":
        conv.LeadTheWay()
        print("6")
        #beh.LeadTheWay
        pass
    elif mystate=="Done":
        print("7")
        pass
    return "Done"

#main
def main():
    state="Init"
    while not state=="Done":
        if state=="My state A":
            state=DoStateA(state)
        elif state=="My state B":
            state=DoStateB()
        elif state=="My state C":
            state=DoStateC()
        elif state=="Init":
            state=DoStateInit()

if __name__=="__main__":
    main()
