from tkinter import *
import math
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer_set=None
window=Tk()
text=Label(text="Timer",fg=GREEN,font=(FONT_NAME,50,"bold"),bg=YELLOW)
text.grid(row=0,column=1)
window.title("timer")
window.config(padx=100,pady=50,bg=YELLOW)
canvas=Canvas(width=200,height=224,bg=YELLOW)
photo=PhotoImage(file="tomato.png")
canvas.create_image(102,112,image=photo)
canva_text=canvas.create_text(100,130,text="00:00",font=(FONT_NAME,35,"bold"),fill="white")
canvas.grid(column=1,row=1)
checkmark=" "

def countdown(c):
    global timer_set
    cm=math.floor(c/60)
    cs=c%60
    if cs<10:
        cs="0"+str(cs)
    canvas.itemconfig(canva_text,text=f"{cm}:{cs}")
    if c>0:

        timer_set=window.after(1000, countdown, c-1)
    else:
        timer()


def timer():
   global checkmark
   global reps
   reps+=1
   if reps%8==0:

       check.config(text=checkmark)
       text.config(text="Break",fg=RED)
       #long break time change whatever you  want
       countdown(2*60)

   elif reps%2==0:
       check.config(text=checkmark)
       text.config(text="Break",fg=PINK)
       #short break time 1 minute
       countdown(1*60)
   else:
       check.config(text=checkmark)
       text.config(text="Work")
       countdown(3*60)
       #work time
       checkmark = "✔" + checkmark


def restart():
    global checkmark
    global reps
    global timer_set
    window.after_cancel(timer_set)
    reps=0
    checkmark=''
    canvas.itemconfig(canva_text, text="00:00")
    text.config(text="Timer", fg=GREEN)


start=Button(text="Start",highlightthickness=0,command=timer)
start.grid(row=2,column=0)
reset=Button(text="Reset",highlightthickness=0,command=restart)
reset.grid(row=2,column=2)
check=Label(text=" ",fg=GREEN,font=(FONT_NAME,35,"bold"),bg=YELLOW)
check.grid(row=3,column=1)
window.mainloop()

