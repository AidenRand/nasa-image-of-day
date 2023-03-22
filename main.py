from tkinter import *
from tkinter import font
from tkcalendar import DateEntry
from PIL import ImageTk
from urllib.request import urlopen
import requests
import json

root = Tk()
root.geometry("1900x1080")
root.title("Nasa Images")
root.config(bg="#d8d8d8")


# Create date entries
entry_font = font.Font(size=14)

year_entry = Entry(root, width=6, font=entry_font)
year_entry.place(x=700, y=25)

seperator1 = Label(root, text="-", font=entry_font)
seperator1.place(x=776, y=25)

month_entry = Entry(root, width=3, font=entry_font)
month_entry.place(x=790, y=25)

seperator1 = Label(root, text="-", font=entry_font)
seperator1.place(x=834, y=25)

day_entry = Entry(root, width=3, font=entry_font)
day_entry.place(x=850, y=25)


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
        root,
        width=40,
        height=27,
        wrap=WORD,
        font=explanation_font,
        bg="#d8d8d8",
    )
    explanation.insert(INSERT, json_data["explanation"])
    explanation.config(state=DISABLED)
    explanation.place(x=1400, y=80)
    print(get_date())
    return image_url


def show_image():
    imageUrl = get_image()
    u = urlopen(imageUrl)
    raw_data = u.read()
    u.close()

    # print photo to window
    image = ImageTk.PhotoImage(data=raw_data)
    label = Label(image=image)
    label.image = image
    label.place(x=70, y=80)


buttonFont = font.Font(size=16)
imageBtn = Button(root, text="Get image", font=buttonFont, command=show_image)
imageBtn.place(x=920, y=19)

# Add scrollbar
sb = Scrollbar(root)
sb.pack(side=RIGHT, fill=Y)

root.mainloop()
