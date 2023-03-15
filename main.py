from tkinter import *
from tkinter import font

root = Tk()
root.geometry("800x800")
root.title("Nasa Images")


def get_user_input():
    input_font = font.Font(size=16)
    user_input = Entry(root, width=30, font=input_font)
    user_input.place(x=180, y=20, height=45)

    enter_input = Button(root, text="🔍", font=input_font, height=1)
    enter_input.place(x=560, y=20)


get_user_input()


root.mainloop()
