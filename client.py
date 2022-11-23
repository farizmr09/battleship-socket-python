import socket      
import threading  
import os
import game

player = game.Game()
player.shipRandom()
player.printBoard()
hit = 15
stop = False

def listen_msg(s):
    global stop, hit
    while True:
        msg = s.recv(1024).decode()
        if ", " in msg:
            y, x = map(int, msg.split(','))
            os.system('cls||clear')
            if player.board[7-x][y] == 1:
                print("Hit!")
                s.send("Hit!".encode())
            else:
                s.send("Miss :(".encode())
            player.board[7-x][y] = "~"
            player.printBoard()
        elif "exit" in msg:
            os.system('cls||clear')
            print("You have lost, booo :p")
            stop = True
            break
        else:
            if "Hit!" in msg:
                hit = hit + 1
                if hit == 16:
                    os.system('cls||clear')
                    print("You have won!!!")
                    stop = True
                    break
            print(msg)

 
s = socket.socket()        
 
port = 12345     
s.connect(('127.0.0.1', port))
threading._start_new_thread(listen_msg, (s, ))

while True:
    if stop:
        s.send("exit".encode())
        s.close()
        break
    msg = input()
    if ", " in msg:
        os.system('cls||clear')
        y, x = map(int, msg.split(','))
        if x > 7 or y > 7:
            print("Out of bound!")
        elif player.oppBoard[7-x][y] == "x":
            s.send(msg.encode())
            player.oppBoard[7-x][y] = "~"
            player.printBoard()
        else:
            player.printBoard()
            print("You've picked that before, please input another coordinate!")
