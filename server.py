import socket  
import threading          

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
print ("Socket successfully created")

port = 12345  
 
s.bind(('', port))    
print ("socket binded to %s" %(port))
 

s.listen(100) 
print ("socket is listening")           

def broadcast(msg, c):
    for host in clients:
        if c != host:
            host.send(msg.encode())

def multi_thread(c, addr):
    print('Got connection from', addr)
    c.send('Thank you for connecting\n'.encode())
    if(len(clients) < 2):
        clientsTurns.append(True)
        c.send('Waiting for another player to join...'.encode())
    else:
        clientsTurns.append(False)
        c.send('Game is starting!\n'.encode())
        broadcast('Game is starting!\n', c)
        while True:
            if clientsTurns[0]:
                c = clients[0]
                c.send("Your turn! Input coordinate (x,y): ".encode())
                broadcast("Waiting for opponent's turn...", c)
                msg = c.recv(1024).decode()
                broadcast(msg, c)
                c = clients[1]
                msg = c.recv(1024).decode()
                if "Hit!" in msg:
                    broadcast(msg, c)
                    continue
                elif "exit" in msg:
                    clients[0].close()
                    clients[1].close()
                    clients.clear()
                    break
                broadcast(msg, c)
                clientsTurns[0] = False
                clientsTurns[1] = True
            else:
                c = clients[1]
                c.send("Your turn! Input coordinate (x,y): ".encode())
                broadcast("Waiting for opponent's turn...", c)
                msg = c.recv(1024).decode()
                broadcast(msg, c)
                c = clients[0]
                msg = c.recv(1024).decode()
                if "Hit!" in msg:
                    broadcast(msg, c)
                    continue
                elif "exit" in msg:
                    clients[0].close()
                    clients[1].close()
                    clients.clear()
                    break
                broadcast(msg, c)
                clientsTurns[1] = False
                clientsTurns[0] = True    

clients = []
clientsTurns = []

while True:
    if(len(clients) < 2):
        c, addr = s.accept()    
        clients.append(c)
        threading._start_new_thread(multi_thread, (c, addr, ))