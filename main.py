from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
YELLOW = "#f7f5dd"
GREEN = "#9bdeac"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    window.config(bg=YELLOW)
    timer_label.config(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
    check_label.config(text="", bg=YELLOW)
    canvas.config(bg=YELLOW)
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break Time", bg=PINK, fg=YELLOW)
        window.config(bg=PINK)
        canvas.config(bg=PINK, highlightthickness=0)
        check_label.config(bg=PINK)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Short Break Time", bg=GREEN, fg=YELLOW)
        window.config(bg=GREEN)
        canvas.config(bg=GREEN, highlightthickness=0)
        check_label.config(bg=GREEN)
    else:
        count_down(work_sec)
        timer_label.config(text="Work Time", bg=RED, fg=YELLOW)
        window.config( bg=RED )
        canvas.config( bg=RED, highlightthickness=0)
        check_label.config(bg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_section = math.floor(reps / 2)
        for _ in range (work_section):
           mark += "✅"
        check_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas= Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(column=2, row=2)

# Label
timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=2, row=0)

check_label= Label(fg=GREEN)
check_label.grid(column=2, row=4)

# Button
start_button = Button(window, text="Start", bg=GREEN, highlightthickness=0, command= start_timer)
start_button.grid(column=0, row=3)

reset_button = Button(window, text="Reset", bg=GREEN, highlightthickness=0, command = reset_timer)
reset_button.grid(column=4, row=3)

window.mainloop()