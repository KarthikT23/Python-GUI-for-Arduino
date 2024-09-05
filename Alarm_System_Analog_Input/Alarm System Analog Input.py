import tkinter as tk
import pyfirmata
from pyfirmata import Arduino, util
from time import sleep
from winsound import Beep
#====================================================================
# Functions
#-----------
def startPOT():
    while flag.get():
        voltage = board.analog[0].read()*5
        if voltage < 2.5:
            if board.digital[2].read(): break
            board.digital[5].write(1)
            board.digital[3].write(0)
            statusLabel.config(text="ALARM", fg='red')
            Beep(500,500)
        else:
            board.digital[5].write(0)
            board.digital[3].write(1)
            statusLabel.config(text="system OK", fg='blue')
            sleep(0.25)
        voltage = round(voltage, 2)
        analogReadLabel.config(text=str(voltage), fg='blue')
        analogReadLabel.update_idletasks()
        win.update()
    board.digital[3].write(0)
    board.digital[5].write(0)
    board.exit()
    win.destroy()
#------------------
def stopPOT():
    flag.set(False)    
#====================================================================
# Arduino board initialization
#------------------------------
board = Arduino("COM12")
board.analog[0].mode = pyfirmata.INPUT
board.digital[2].mode = pyfirmata.INPUT
it = pyfirmata.util.Iterator(board)  
it.start()
#------------
# GUI design
#------------
win = tk.Tk()
win.title("SYSTEM")
win.minsize(220,100)
#---------------------------------------------------------
descriptionLabel = tk.Label(win, text="  POT Voltage :")
descriptionLabel.grid(column=1, row=1)
analogReadLabel = tk.Label(win, text="0.00", fg='blue')
analogReadLabel.grid(column=2, row=1)
unitLabel = tk.Label(win, text="Volts")
unitLabel.grid(column=3, row=1)
#---------------------------------------------------------
seperatorLabel1 = tk.Label(win, text="----------------")
seperatorLabel1.grid(column=1, row=2)
seperatorLabel2 = tk.Label(win, text="------")
seperatorLabel2.grid(column=2, row=2)
seperatorLabel3 = tk.Label(win, text="------")
seperatorLabel3.grid(column=3, row=2)
#---------------------------------------------------------
flag = tk.BooleanVar(win)
flag.set(True)
#---------------------------------------------------------
startBtn = tk.Button(win, bd=4, bg='#90EE90', text="START", command=startPOT)
startBtn.grid(column=1, row=3)
stopBtn = tk.Button(win, bd=4, bg='#FF6666', text="STOP", command=stopPOT)
stopBtn.grid(column=4, row=3)
#---------------------------------------------------------
statusLabel = tk.Label(win, text="system OFF")
statusLabel.grid(column=1, row=4)
#---------------------------------------------------------
win.mainloop()