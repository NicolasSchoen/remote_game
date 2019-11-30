import tkinter as tk
from tkinter import messagebox
from functools import partial
import time
import keyboard
import math

isOn = True
serverOn = []
size = 28


def toggleOn():
    global isOn

    if(isOn):
        btnOn.config(bg="orange")
        if(messagebox.askyesno("Exit Application", "Do you want to close the application?")):
            exit(0)
    else:
        btnOn.config(bg="lightgreen")
    isOn = not isOn


def toggleServer(servnr):

    if(not serverOn[servnr]):
        btnServ[servnr].config(bg="green")
    else:
        servstring = "Would you like to shutdown server " + str(servnr) + "?"
        if(messagebox.askokcancel("Server Shutdown", servstring)):
            serverOn[servnr] = not serverOn[servnr]
            btnServ[servnr].config(bg="red")
            servstring = "server " + str(servnr) + " is now offline!"
            messagebox.showinfo("Serverinfo", servstring)


def synchronise():
    pass



#gui initialisation
app = tk.Tk()

#images
imgon = tk.PhotoImage(file="icons\\on.png")
imgserv = tk.PhotoImage(file="icons\\server.png")
imgsyn = tk.PhotoImage(file="icons\\synchronise.png")

#buttons
#entrySize = tk.Entry(text="2")
btnOn = tk.Button(image=imgon, bg="lightgreen", text="on", command=lambda: toggleOn())
btnSyn = tk.Button(image=imgsyn, bg="white", text="on", command=lambda: synchronise())
btnServ = []

#add new server here
for i in range(size):
    btnServ.append(tk.Button(image=imgserv, bg="green", command=partial(toggleServer, (i))))
#btnServ.append(tk.Button(image=imgserv, bg="green", command=lambda: toggleServer(1)))


#canvas = tk.Canvas(width=300, height=300, bg="grey")


#player = canvas.create_rectangle(posx,posy,posx + pwidth,posy + pheight, fill="white")


#place buttons
btnOn.grid(row=0, column=0)
btnSyn.grid(row=1, column=0)
#entrySize.grid(row=2, column=0)
#canvas.grid(row=0, column=2)
z=0
for i in range(len(btnServ)):
    if(i%5 == 0):
        z+=1
    btnServ[i].grid(row=i%5, column=1+z)
    serverOn.append(True)
    print(i)

app.mainloop()