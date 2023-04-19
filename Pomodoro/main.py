import base64
import tkinter
import os
from tomato_png import img as tomato_pic
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
MINUTES = 60
timer = None
mode = 0

# ---------------------------- ADD PICTURE TO EXECUTABLE FILE------------------------------- #
tomato = open('tomato_tmp.png', 'wb')
tomato.write(base64.b64decode(tomato_pic))
tomato.close()


# ---------------------------- TIMER RESET ------------------------------- # 
# 25 5 25 5 25 5
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_pomodoro():
    global mode
    mode += 1
    if mode == 8:
        mode = 0
        count = LONG_BREAK_MIN * MINUTES
        timer_title.config(text="Long Break", fg=RED)
    elif mode % 2 == 0:
        count = SHORT_BREAK_MIN * MINUTES
        timer_title.config(text="Short Break", fg=PINK)
    else:
        count = WORK_MIN * MINUTES
        timer_title.config(text="Work Time", fg=GREEN)
    count_down(count)


def reset_pomodoro():
    window.after_cancel(timer)
    timer_title.config(text="Timer", fg=GREEN)
    canvas.itemconfig(counter_text, text="00:00")
    checkmark.config(text="")
    global mode
    mode = 0


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    remaining_minutes = str(int(count / 60)).zfill(2)
    remaining_seconds = str((count % 60)).zfill(2)
    canvas.itemconfig(counter_text, text=f"{remaining_minutes}:{remaining_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_pomodoro()
        global mode
        text = "✔" * int(mode/2)
        checkmark.config(text=text)


# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = tkinter.Canvas(width=210, height=230, bg=YELLOW, highlightthickness=0)
tomato_image = tkinter.PhotoImage(file="tomato_tmp.png")
# You can change "tomato_tmp.png" back into "tomato.png" when using python.
canvas.create_image(106, 113, image=tomato_image)

counter_text = canvas.create_text(106, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


timer_title = tkinter.Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_title.grid(column=1, row=0)


start_button = tkinter.Button(text="Start", command=start_pomodoro, font=(FONT_NAME, 20, "bold"), highlightthickness=0)
start_button.grid(column=0, row=2)
reset_button = tkinter.Button(text="Reset", command=reset_pomodoro, font=(FONT_NAME, 20, "bold"), highlightthickness=0)
reset_button.grid(column=2, row=2)

checkmark = tkinter.Label(text="", fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)

window.mainloop()

os.remove('tomato_tmp.png')
