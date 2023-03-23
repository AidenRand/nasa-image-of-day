from tkinter import *
from tkinter import font
from tkinter import ttk
from PIL import ImageTk
from urllib.request import urlopen
import requests
import json

root = Tk()
root.geometry("1900x1080")
root.title("Nasa Images")
root.config(bg="#d8d8d8")

# Add a main_frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

# Create a canvas
page_canvas = Canvas(main_frame)
page_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add page scrollbar
page_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=page_canvas.yview)
page_scrollbar.pack(side=RIGHT, fill=Y)

# Configure canvas
page_canvas.configure(yscrollcommand=page_scrollbar.set)
page_canvas.bind(
    "<Configure>", lambda e: page_canvas.configure(scrollregion=page_canvas.bbox("all"))
)

# Create another frame in canvas
second_frame = Frame(page_canvas)

# Add new frame to a window in the canvas
page_canvas.create_window((0, 0), window=second_frame, anchor="nw")


# Create date entries
entry_font = font.Font(size=14)

year_entry = Entry(second_frame, width=6, font=entry_font)
year_entry.grid(row=1, column=0)

seperator1 = Label(second_frame, text="-", font=entry_font)
seperator1.place(x=776, y=25)

month_entry = Entry(second_frame, width=3, font=entry_font)
month_entry.grid(row=1, column=4)

seperator1 = Label(second_frame, text="-", font=entry_font)
seperator1.grid(row=1, column=5)

day_entry = Entry(second_frame, width=3, font=entry_font)
day_entry.grid(row=1, column=8)


# Get image date
def get_date():
    whole_date = (
        str(year_entry.get())
        + "-"
        + str(month_entry.get())
        + "-"
        + str(day_entry.get())
    )
    return whole_date


def get_image():
    url = "https://api.nasa.gov/planetary/apod?api_key=tgdFlsc0ek07wdiX6UI5RDFH0793AzMD5YQi0DWE"

    print(get_date())
    params = {"hd": "True", "date": get_date()}

    # get json data from api
    response = requests.get(url, params=params)
    json_data = json.loads(response.text)
    image_url = json_data["url"]

    # Print image explanation
    explanation_font = font.Font(size=14)
    explanation = Text(
        second_frame,
        width=40,
        height=27,
        wrap=WORD,
        font=explanation_font,
        bg="#d8d8d8",
    )
    explanation.insert(INSERT, json_data["explanation"])
    explanation.config(state=DISABLED)
    explanation.grid(row=10, column=10)
    print(get_date())
    return image_url


def show_image():
    imageUrl = get_image()
    u = urlopen(imageUrl)
    raw_data = u.read()
    u.close()

    # print photo to window
    image = ImageTk.PhotoImage(data=raw_data)
    label = Label(second_frame, image=image)
    label.image = image
    label.grid(row=0, column=0)


buttonFont = font.Font(size=16)
imageBtn = Button(
    second_frame, text="Get image", font=buttonFont, command=show_image
).grid(row=-1, column=100)


my_label = Label(second_frame, text="hello").grid(row=3, column=2)


root.mainloop()
