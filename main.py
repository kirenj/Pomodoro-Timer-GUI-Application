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
CHECK_MARK = "✔"
REPS = 0
TIMER = "" #(Initally we leave this at 0)


# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global REPS    
    REPS = 0
    # the below window.after_cancel will be used to cancel the TIMER variable that was initialized in the countdown function
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label["text"] = "Timer"
    timer_label["fg"] = GREEN
    checkmark_label["text"] = ""


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if REPS % 8 == 0:
        countdown(long_break_sec)
        timer_label["text"] = "Break!"
        timer_label["fg"] = RED
    elif REPS % 2 == 0:
        countdown(short_break_sec)
        timer_label["text"] = "Break!"
        timer_label["fg"] = PINK
    else:
        countdown(work_sec)
        timer_label["text"] = "Work!"
        timer_label["fg"] = GREEN




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    min_count = math.floor(count / 60)
    sec_count = count % 60
    if sec_count == 0:
        sec_count = "00"
    for i in range (0, 10):
        if sec_count == i:
            sec_count = f"0{sec_count}"
    # window.after instructs the program to do something after a set amount of time (ms)
    # Inorder to edit/ cancel the below, we need to put this in a variable and make it a global variable
    if count > 0:
        global TIMER
        TIMER = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        work_session = math.floor(REPS/2)
        marks = ""
        for i in range(work_session):
            marks += CHECK_MARK
        checkmark_label["text"] = marks
    # timer_text is the variable we created in the canvas module to replace the text with the below code
    canvas.itemconfig(timer_text, text=f"{min_count}:{sec_count}")
    # The 'itemconfig' is a method that is used only with 'Canvas' class, pass in the item you want to configure
    # and insert the item you want to configure it with


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
# window.config(height=)
window.config(pady=50, padx=100, bg=YELLOW)



canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
# we need to place the create_text in a variable so that we can change the text to the timer shown in the countdown function
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)
# #the function has to be placed here to avoid errors
# countdown(5)

timer_label = Label(text="Timer", font=("harrington", 35, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", bg='white', fg='black', highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg='white', fg='black', highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)

checkmark_label = Label(fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=3)












window.mainloop()