import os # Import external function libraries
import time
#################################
A = "   " # Declaration of global variables
B = "   "
C = "   "
Running = True
move = 1
#################################
# My functions
def xWinCheck(): # "X" player winning check
    if (A == "XXX" or B == "XXX" or C == "XXX" or (A[0] == "X" and 
    B[0] == "X" and C[0] == "X") or (A[1] == "X" and B[1] == "X" and 
    C[1] == "X") or (A[2] == "X" and B[2] == "X" and C[2] == "X") or 
    (A[0] == "X" and B[1] == "X" and C[2] == "X") or (A[2] == "X" and 
    B[1] == "X" and C[0] == "X")):
        return True
    else:
        return False
#####
def oWinCheck(): # "O" player winning check
    if (A == "OOO" or B == "OOO" or C == "OOO" or (A[0] == "O" and 
    B[0] == "O" and C[0] == "O") or (A[1] == "O" and B[1] == "O" and 
    C[1] == "O") or (A[2] == "O" and B[2] == "O" and C[2] == "O") or 
    (A[0] == "O" and B[1] == "O" and C[2] == "O") or (A[2] == "O" and 
    B[1] == "O" and C[0] == "O")):
        return True
    else:
        return False
#####
def FullCheck(): # The table is full?
    if A.find(" ") ==  -1 and B.find(" ") ==  -1 and C.find(" ") == -1:
        return True
    else:
        return False
#####
def StepCheck(step): # inputcheck
    if ((step == "A1" and A[0] == " ") or (step == "A2" and A[1] == " ") or 
    (step == "A3" and A[2] == " ") or (step == "B1" and B[0] == " ") or 
    (step == "B2" and B[1] == " ") or (step == "B3" and B[2] == " ") or 
    (step == "C1" and C[0] == " ") or (step == "C2" and C[1] == " ") or 
    (step == "C3" and C[2] == " ")):
        return False
    else:
        return True
#####
def stringReplaceI(string,where,what): # Character replacing at index in a string 
    tempS = ""
    for i in range(len(string)):
        if i != int(where):
            tempS += string[i]
        else:
            tempS += what
    return tempS
#####
def stepSave(step, playersign): # Saving the step
    global A, B, C
    if step == "A1":
        A = stringReplaceI(A,0,playersign)
    elif step == "A2":
        A = stringReplaceI(A,1,playersign)
    elif step == "A3":
        A = stringReplaceI(A,2,playersign)
    elif step == "B1":
        B = stringReplaceI(B,0,playersign)
    elif step == "B2":
        B = stringReplaceI(B,1,playersign)
    elif step == "B3":
        B = stringReplaceI(B,2,playersign)
    elif step == "C1":
        C = stringReplaceI(C,0,playersign)
    elif step == "C2":
        C = stringReplaceI(C,1,playersign)
    elif step == "C3":
        C = stringReplaceI(C,2,playersign)
    Visual()
#####   
def Visual(): # Visual representation
    os.system("clear")
    print()
    print("                       Put")
    print()
    print("                       your")
    print()
    print("                    Game Face")
    print()
    print("                        ON!")
    print()
    print("              TicTac (ver. Beta 1.01)")
    print()
    print("                    1   2   3")
    print("                   -----------")
    print("                A |",end="")
    for i in (A):
        print(" " + i + " |",end="")
    print()
    print("                   -----------")
    print("                B |",end="")
    for i in (B):
        print(" " + i + " |",end="")
    print()
    print("                   -----------")
    print("                C |",end="")
    for i in (C):
        print(" " + i + " |",end="")
    print()
    print("                   -----------")
    print()
#####
def Again(): # Game again?
    global A,B,C,move
    while True:
        Visual()
        end = input("     Would you like to play again? (Y / N): ")
        if end == "N":
            return False
        elif end == "Y":
            A = "   "
            B = "   "
            C = "   "
            move = 0
            return True
#####
def Joke(): # Joke part
    while True: 
        demo = ""
        print()
        demo = input("                            Who would like to play BATTLESHIP?!!!")
        print()
        demo = input("                           ME TOO, but sadly it is not ready, yet...")
        print()
        demo = input("                          So, until then let's play some Tic Tac Toe!")
        break

############################################

# Main part start
os.system("clear")
Joke() # Just for fun
while Running: 
    Visual()
    if move % 2 == 0:
        print("           This is the O player's round")
        print()
    else:
        print("           This is the X player's round")
        print()
    inputOk = True
    while inputOk: # Input part
        Step = input("          Please type in your next step: ")
        inputOk = StepCheck(Step) # Calling the input checking function
        if inputOk == False:
            pass
        else:
            print()
            print("                Try again!")
            time.sleep(1)
            Visual()
    if move % 2 == 0:
        stepSave(Step,"O")
    else:
        stepSave(Step,"X")
    if xWinCheck() == True: # Checking if X the winner
        for i in range(3):
            print("                The Winner is X!")
            time.sleep(1)
        print()
        Running = Again()
    if oWinCheck() == True: # Checking if O the winner
        for i in range(3):
            print("                The Winner is O!")
            time.sleep(1)
        print()
        Running = Again()
    if FullCheck() == True and xWinCheck() == False and oWinCheck() == False: # Checking if it is a Tie
        for i in range(3):
            print("                  It is a Tie!")
            time.sleep(1)
        print()
        Running = Again()
    move += 1
###### Main part end
