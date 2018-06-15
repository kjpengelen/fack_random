# import statements
import behaviors as beh
import converse as conv

#globals (preferably not)

dialogone=True
dialogtwo=False
actionone=False

# Step 1
if dialogone==True:
    conv.Greeting()
    print("end cycle 1")
    dialogone=False
    dialogtwo=True

# Step 2
if dialogtwo==True:
    conv.OfferHelp()
    dialogtwo=False
    actionone=True

# Step 3

if actionone==True:
    nao.Say("Bye")
    actionone=False
