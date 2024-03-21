from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Calibri"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        long_break_sec = 60 * LONG_BREAK_MIN
        count_down(long_break_sec)
        label_timer.config(text="Break", fg=RED)

    elif reps % 2 == 1:
        work_sec = 60 * WORK_MIN
        count_down(work_sec)
        label_timer.config(text="Work", fg=GREEN)

    else:
        short_break_sec = 60 * SHORT_BREAK_MIN
        count_down(short_break_sec)
        label_timer.config(text="Break", fg=PINK)


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
        window.after(1000, count_down, count-1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodore")
window.config(padx=100, pady=50, bg=YELLOW)

# ---Creating the Canvas
canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)

# ---Adding the image on canvas
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(101, 112, image=tomato_img)
# ---Adding the text on canvas
timer_text = canvas.create_text(101, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)




# ---Adding the other Widgets
label_timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, ))
label_timer.grid(column=1, row=0)

start_button = Button(text="Start", width=7, bg=YELLOW, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", width=7, bg=YELLOW, highlightthickness=0)
reset_button.grid(column=2, row=2)

check_mark = Label(text="✔", fg=GREEN, bg=YELLOW, font=50)
check_mark.grid(column=1, row=3)













window.mainloop()





