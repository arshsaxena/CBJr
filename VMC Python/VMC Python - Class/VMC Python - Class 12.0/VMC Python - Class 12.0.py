#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## User vs Computer
#User will be player 1 and Computer will be plyaer 2
import random

def checkBoard(board):
    for player in range(1,3):
        if player==1:
            symbol="X"
        else:
            symbol="O"
        for i in range(0,3):
            if (board[i][0]==symbol) and (board[i][1]==symbol) and (board[i][2]==symbol):
                return player+1
        for i in range(0,3):
            if (board[0][i]==symbol) and (board[1][i]==symbol) and (board[2][i]==symbol):
                return player+1
    
        if (board[0][0]==symbol) and (board[1][1]==symbol) and (board[2][2]==symbol):
                return player+1

        if (board[0][2]==symbol) and (board[1][1]==symbol) and (board[2][0]==symbol):
                return player+1


    for i in range(0,3):
        for j in range(0,3):
            if board[i][j]=="":
                return 0
    return 1

def initializeBoard(board):
    for i in range(0,3):
        for j in range(0,3):
            board[i][j]=""


def printBoard(board):
    #write code to print the current board of the game
    cellstr=""
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j]=="":
                cellstr=" "
            elif board[i][j]=="X":
                cellstr="X"
            else:
                cellstr="O"
            print("|",cellstr,end=" ")
        print("|")
        if i<2:
            print("|---|---|---|")
    print()

def whoWillStart():
    #returns who will start the game
    return random.randint(1, 2)

def startGame(board,players,player):
    initializeBoard(board)
    players[1]=input("Enter name of the player (symbol X): ")
    #players[2]=input("Enter name of the Player 2 (symbol O): ")
    print()
    print(players[player],"won the toss. So", players[player], "will start first.")
    print()


def playMove(board,players,player):    
    print(players[player]," will take move now.")
    row=int(input("Choose Row where you want to put your bet: ")) 
    column=int(input("Choose Column where you want to put your bet: ")) 
    board[row-1][column-1]="X"            
    printBoard(board)

def computerMove(board,players,player):   
    print(players[player], "has taken the move. Check below: ")
    #checking row for winning
    for i in range(3):
        if board[i].count("O")==2:
            for j in range(3):
                if board[i][j]=="":
                    board[i][j]="O"
                    printBoard(board)
                    return   
    for i in range(3):
        count=0
        for j in range(3):
            if board[j][i]=="O":
                count+=1
        if count==2:
            for j in range(3):
                if board[j][i]=="":
                    board[j][i]="O"
                    printBoard(board)
                    return
 #Check for primary diagonal           
    countO=0
    locationE=-1
    for i in range(3):
        if board[i][i]=="O":
            countO+=1
        if board[i][i]=="":
            locationE=i
    if countO==2 and locationE!=-1:
        board[locationE][locationE]="O"
        printBoard(board)
        return
   
        
 #Check other diagonal
    countO=0
    locationE=-1
    for i in range(3):
        if board[i][2-i]=="O":
            countO+=1
        if board[i][2-i]=="":
            locationE=i
    if countO==2 and locationE!=-1:
        board[locationE][2-locationE]="O"
        printBoard(board)
        return
   

#Counter Move 
    for i in range(3):
        if board[i].count("X")==2:
            for j in range(3):
                if board[i][j]=="":
                    board[i][j]="O"
                    printBoard(board)
                    return
   
    for i in range(3):
        count=0
        placed=0
        for j in range(3):
            if board[j][i]=="X":
                count+=1
        if count==2:
            for j in range(3):
                if board[j][i]=="":
                    board[j][i]="O"
                    printBoard(board)
                    return
                
 #Check for primary diagonal           
    countO=0
    locationE=-1
    for i in range(3):
        if board[i][i]=="X":
            countO+=1
        if board[i][i]=="":
            locationE=i
    if countO==2 and locationE!=-1:
        board[locationE][locationE]="O"
        printBoard(board)
        return
        
 #Check other diagonal
    countO=0
    locationE=-1
    for i in range(3):
        if board[i][2-i]=="X":
            countO+=1
        if board[i][2-i]=="":
            locationE=i
    if countO==2 and locationE!=-1:
        board[locationE][2-locationE]="O"
        printBoard(board)
        return
#computer has to place her non-critical bet
#preferred positions are center and then corners    
    if board[1][1]=="":
        board[1][1]="O"
        printBoard(board)
        return

    if board[0][0]=="":
        board[0][0]="O"
        printBoard(board)
        return

    if board[0][2]=="":
        board[0][2]="O"
        printBoard(board)
        return
    
    if board[2][0]=="":
        board[2][0]="O"
        printBoard(board)
        return

    if board[2][2]=="":
        board[2][2]="O"
        printBoard(board)
        return

    for i in range(3):
        for j in range(3):
            if board[i][j]=="":
                board[i][j]="O"
                printBoard(board)
                return

def togglePlayer(playerInGame):
    if playerInGame==1:
        return 2
    else:
        return 1


def announceResult(state,states,players):    
    if states[state]=="DRAW":
        print("Game results in a draw.")
    elif states[state]=="P1-WIN":
        print(players[1], "won the game. Congratulations!!")
    elif states[state]=="P2-WIN":
        print(players[2], "won the game. Congratulations!!")

    print()
    return int(input("Do you want to play again? (Enter 1 for yes, 0 for no): "))


def restartGame(board,players,whoStarted):
    initializeBoard(board)
    whoStarted=togglePlayer(whoStarted)
    print()
    print("In this game", players[whoStarted], " will start the game.")
    print()
    return whoStarted
    

#Main Program

# Variables

board=[["","X",""],["X","O","X"],["","","O"]]

players=["","P1","Computer"]

states=["PLAY", "DRAW", "P1-WIN", "P2-WIN"]

playerInGame=0
state=0
whoStarted=0

# Main Program

playerInGame=whoWillStart()
whoStarted=playerInGame
startGame(board,players,whoStarted)

# Game Loop


while True:
    # check whose turn is to put the bet and then take the move
    
    if playerInGame==1:
        playMove(board,players,playerInGame)
    else:
        computerMove(board,players,playerInGame)    

    #check the condition of the board    
    state=checkBoard(board)
    
    if states[state]=="PLAY":
       playerInGame=togglePlayer(playerInGame)
    else:
        playMore=announceResult(state,states,players)

        if playMore==1:
            playerInGame=restartGame(board,players,whoStarted)
            whoStarted=playerInGame
        else:
            print("Thanks for playing game!")
            break

