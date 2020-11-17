#David Faulkner Katz
#Tic Tac Toe
def makeBoard():
    s=" "
    board=[[s,s,s],[s,s,s],[s,s,s]]
    return board

def pb(board):
    print(" |1|2|3|")
    for i in range(len(board)):
        line=chr(i+65)+"|"
        for s in board[i]:
            line+=s+"|"
        print(line)

def isfree(spot, board):
    if board[ord(spot[0])-65][spot[1]]==" ":
        return True
    else:
        return False

def entermove(board,spot,move):
    board[ord(spot[0])-65][spot[1]]=move[1]
    return board
        
def makeMove(move, board):
    pb(board)
    print("It is currently "+move[1]+"'s turn")
    print("Please select a move in the form Row+Column i.e. A2")
    val=False
    while not val:
        spot=input("Enter move: ").upper()
        spot=[spot[0],int(spot[1])-1]
        if len(spot)==2 and "A"<=spot[0]<="C" and 0<=spot[1]<=2:
            if isfree(spot, board):
                val=True
            else:
                print("That spot is taken, enter a move for an empty spot.")
        else:
            print("Thats not a valid move")
    board=entermove(board,spot,move)
    return board

def canMove(board):
    cm=False
    for r in board:
        for s in r:
            if s==" ":
                cm=True
                break
    return cm

def whoWon(board):
    winner=" "
    for i in range(3):
        if winner==" " and board[i][0]==board[i][1]==board[i][2]:
            winner=board[i][0]
        elif winner==" " and board[0][i]==board[1][i]==board[2][i]:
            winner=board[0][i]
    if winner==" ":
        if board[0][0]==board[1][1]==board[2][2]:
            winner=board[0][0]
        elif board[0][2]==board[1][1]==board[2][0]:
            winner=board[0][2]
    return winner
        

def main():
    board=makeBoard()
    move=[True,"X"]
    while move[0]:
        board=makeMove(move, board)
        if move[1]=="X":
            move[1]="O"
        else:
            move[1]="X"
        winner=whoWon(board)
        if winner!=" ":
            break
        move[0]=canMove(board)
    winner=whoWon(board)
    if winner==" ":
        winner="no one, it's a tie"
    print("Winner is "+winner)
    pb(board)
    
main()
