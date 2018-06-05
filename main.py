# import statements
import behaviors as beh
import time

#globals (preferably not)

#function definitions
def DoStateInit():
    """Do initialiazation"""
    
    beh.InitRobot()
    
    return "To basicWave"
    
def action1(mystate):
    """Execute basicWave"""

    time.sleep(0)
    if mystate=="To basicWave":
        beh.basicWave()
        pass
    elif mystate=="To followMe":
        pass
    return "To followMe"

def action2():
    """Execute followMe"""

    time.sleep(5)
    beh.followMe()
    return "Done"

#main
def main():
    state="Init"
    while not state=="Done":
        if state=="To basicWave":
            state=action1(state)
        elif state=="To followMe":
            state=action2()
        elif state=="Init":
            state=DoStateInit()

if __name__=="__main__":
    main()
    

