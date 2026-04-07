from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

tomato_image = PhotoImage(file="intermediate/pomodoro/tomato.png")
canvas = Canvas(width=210, height=240, bg=YELLOW, highlightthickness=0)
canvas.create_image(103, 120, image=tomato_image)
canvas.create_text(103, 140, text="00:00",font=(FONT_NAME,35,"bold"), fill= "white")
canvas.grid(column=1,row=1)

timer_label = Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,40,"bold"))
timer_label.grid(column=1,row=0)

start_button = Button(text="Start")
start_button.grid(column=0,row=2)

stop_button = Button(text="Stop")
stop_button.grid(column=2,row=2)

checkmark_label = Label(text="✔",bg=YELLOW,fg=GREEN,font=(FONT_NAME,10,"bold"))
checkmark_label.grid(column=1,row=3)


window.mainloop()
