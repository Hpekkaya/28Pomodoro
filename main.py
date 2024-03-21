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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5*60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count-1)

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





