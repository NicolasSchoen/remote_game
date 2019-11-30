from tkinter import *
import time
import threading
import socket
import keyboard




#---------simple game---------------------------------------------------------------------------------------------------
#
#----------------------         controls:
#
#----------------------         move up:       w
#----------------------         move down:     s
#----------------------         move right:    d
#----------------------         move left:     a
#-----------------------------------------------------------------------------------------------------------------------


#variables
width = 500             #width of the area
height = 500            #height of the area
posx = 50               #player pos x
posy = 50               #player pos y
eposx = 0               #enemy pos x
eposy = -50             #enemy pos y
pwidth = 50             #width of player
pheight = 50            #height of player
counter = 0             #score
pspeed = 10             #speed of the player
espeed = 5             #speed of the enemy
isAlive = True          #true if player is alive
pDirection = 0          #direction of the player(0=not moving, 1=up, 2=down, 3=right, 4=left)
started = False




#functions
def moveRight():
    global posx

    if(posx < width - pwidth):
        posx += pspeed
        canvas.move(player, pspeed, 0)

def moveLeft():
    global posx

    if(posx > 0):
        posx -= pspeed
        canvas.move(player, -pspeed, 0)

def moveUp():
    global posy

    if(posy > 0):
        posy -= pspeed
        canvas.move(player, 0, -pspeed)

def moveDown():
    global posy

    if(posy < height - pheight):
        posy += pspeed
        canvas.move(player, 0, pspeed)

def movePlayer():
    global posx
    global posy
    global pDirection

    #(0=not moving, 1=up, 2=down, 3=right, 4=left)
    if(pDirection == 1):
        moveUp()
    elif(pDirection == 2):
        moveDown()
    elif (pDirection == 3):
        moveRight()
    elif (pDirection == 4):
        moveLeft()


def moveEnemy():
    global canvas
    global isDead
    global enemy

    if(isAlive):
        checkDirection()

def checkDirection():
    global posx
    global posy
    global eposx
    global eposy
    global canvas
    global espeed

    #get player pos

    #calc direction
    dirx=0
    diry=0
    if(posx != eposx):
        if(posx > eposx):
            eposx += espeed
            dirx = espeed
        else:
            eposx -= espeed
            dirx = -espeed
    if(posy != eposy):
        if (posy > eposy):
            eposy += espeed
            diry = espeed
        else:
            eposy -= espeed
            diry = -espeed

    #move enemy
    canvas.move(enemy, dirx, diry)


def checkAlive():
    global isAlive
    global player
    global enemy

    #if(posx+pwidth > eposx and posx+pwidth < eposx+pwidth and posy+pheight > eposy and posy+pheight < eposy+pheight):
    if(posx+pwidth > eposx and posx < eposx+pwidth and posy+pheight > eposy and posy < eposy+pheight):
        isAlive = False
        print("dead")
        canvas.delete(player)
        canvas.itemconfig(enemy, fill="red")


def checkWaittime(ctr):
    wt= 0.1
    if (ctr > 100):
        wt = 10 / ctr

    return wt




#GameLoop
def gameloop():
    global counter
    global isAlive
    global started
    global client

    waittime = 1.0
    while isAlive:
        if(started):
            waittime = checkWaittime(counter)
            time.sleep(waittime)
            counter += 1
            lbltext="Score: " + str(counter)
            label.config(text=lbltext)
            movePlayer()
            moveEnemy()
            checkAlive()


#draw screen
gui = Tk()


def receiveMsg():
    global isAlive
    global pDirection
    global started
    global serverSocket
    # configure and start server
    #serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(('', 15151))
    serverSocket.listen(1)
    print("waiting for connection")
    print("Server started!\n\n")
    while True:
        #client, addr = serverSocket.accept()
        #print("connection established")
        #started = True

        while isAlive:
            client, addr = serverSocket.accept()
            print("connection established")
            started = True
            sentence = client.recv(1024).decode()
            if (sentence == "up"):
                pDirection = 1
                client.send("ok".encode())
            if (sentence == "down"):
                pDirection = 2
                client.send("ok".encode())
            if (sentence == "right"):
                pDirection = 3
                client.send("ok".encode())
            if (sentence == "left"):
                pDirection = 4
                client.send("ok".encode())
            client.close()

def key(event):
    global pDirection

    kp = repr(event.char)
    print("pressed", kp) #repr(event.char))
    # (0=not moving, 1=up, 2=down, 3=right, 4=left)
    if(event.char == 'w'):
        pDirection = 1
    if(event.char == 'a'):
        pDirection = 4
    if(event.char == 's'):
        pDirection = 2
    if(event.char == 'd'):
        pDirection = 3


stest = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
stest.connect(("8.8.8.8", 80))

ipadrtext= "Please connect to: " + stest.getsockname()[0] + ":15151"
stest.close()

label = Label(text=ipadrtext)
label.pack()

canvas = Canvas(width=width, height=height, bg="grey")
canvas.pack()

player = canvas.create_rectangle(posx,posy,posx + pwidth,posy + pheight, fill="white")
enemy = canvas.create_rectangle(eposx, eposy, eposx+pwidth, eposy+pheight, fill="yellow")

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

threading._start_new_thread(gameloop,())
threading._start_new_thread(receiveMsg,())
gui.bind("<Key>", key)

gui.mainloop()