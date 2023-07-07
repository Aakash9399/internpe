import random
board=['-','-','-',
       '-','-','-',
       '-','-','-']
currentPlayer='X'
winner=None
GameRunning=True

def printboard(board):
    print(board[0]+" | "+board[1]+" | "+board[2])
    print("---------")
    print(board[3]+" | "+board[4]+" | "+board[5])
    print("---------")
    print(board[6]+" | "+board[7]+" | "+board[8])
printboard(board)

def playerinput(board):
    inp=int(input("enter number between 1-9: "))
    if inp>=0 and inp<=9 and board[inp-1]=="-":
        board[inp-1]=currentPlayer
    else:
        print(" Oops player is already in that spot!")

def checkhorizontal(board):
    global winner
    if board[0]==board[1]==board[2] and board[1]!="-":
        winner=board[0]
        return True
    elif board[3]==board[4]==board[5] and board[3]!="-":
        winner=board[3]
        return True
    elif board[6]==board[7]==board[8] and board[6]!="-":
        winner=board[6]
        return True
    
def checkrow(board):
    global winner 
    if board[0]==board[3]==board[6] and board[0]!="-":
        winner=board[0]
        return True
    elif board[1]==board[4]==board[7] and board[1]!="-":
        winner=board[1]
        return True
    elif board[2]==board[5]==board[8] and board[2]!="-":
        winner=board[2]
        return True
    
def checkdiag(board):
    global winner
    if board[0]==board[4]==board[8] and board[0]!="-":
        winner=board[0]
        return True
    elif board[2]==board[4]==board[6] and board[2]!="-":
        winner=board[2]
        return True
    
def checktie(board):
    if "-"  not in board:
        printboard(board)
        print("it is a tie!")
        GameRunning=True

def checkwin(board):
    if checkdiag(board) or checkhorizontal(board) or checkrow(board):
        print(f"The winner is {winner}")

def switchplayer(board):
    global currentPlayer
    if currentPlayer=="X":
        currentPlayer="O"
    else:
        currentPlayer="X"

def computer(board):
    while currentPlayer=="O":
        position=random.randint(0,8)
        if board[position]=="-":
            board[position]="O"
            switchplayer(board)
    

while GameRunning:
    printboard(board)
    playerinput(board)
    checkwin(board)
    checktie(board)
    switchplayer(board)
    computer(board)
    checkwin(board)
    checktie(board)