from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ""

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer",fg=GREEN)
    checkmark_label.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_Seconds = LONG_BREAK_MIN * 60
    countdown_seconds = 0

    if reps % 2 != 0:
        countdown_seconds = work_seconds
        timer_label.config(text="Work",fg=GREEN)
    elif reps % 2 == 0 and reps != 8:
        countdown_seconds = short_break_seconds
        timer_label.config(text="Break",fg=PINK)
    else:
        countdown_seconds = long_break_Seconds
        timer_label.config(text="Break",fg=RED)

    start_countdown(countdown_seconds)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def start_countdown(count):
    global timer
    check_mark = ""
    work_sessions = math.floor(reps/2)

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, start_countdown, count-1)
    
    for session in range(work_sessions):
        check_mark += "✔"
    checkmark_label.config(text=check_mark)
         

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

tomato_image = PhotoImage(file="intermediate/pomodoro/tomato.png")
canvas = Canvas(width=210, height=240, bg=YELLOW, highlightthickness=0)
canvas.create_image(103, 120, image=tomato_image)
timer_text = canvas.create_text(103, 140, text="00:00",font=(FONT_NAME,35,"bold"), fill= "white")
canvas.grid(column=1,row=1)

timer_label = Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,40,"bold"))
timer_label.grid(column=1,row=0)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2,row=2)

checkmark_label = Label(bg=YELLOW,fg=GREEN,font=(FONT_NAME,10,"bold"))
checkmark_label.grid(column=1,row=3)


window.mainloop()
