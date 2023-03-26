from tkinter import *
from tkinter import font
from PIL import ImageTk
from urllib.request import urlopen
from datetime import date
import webbrowser
import requests
import json
from PIL import Image, ImageTk

root = Tk()
root.geometry("1900x1080")
root.title("Nasa Images")
root.config(bg="#d8d8d8")

# Get todays date
today = date.today()

year = today.strftime("%Y")
month = today.strftime("%m")
day = today.strftime("%d")


# Create date entries
entry_font = font.Font(size=14)

year_entry = Entry(root, width=6, font=entry_font)
year_entry.place(x=700, y=25)
year_entry.insert(0, year)

seperator1 = Label(root, text="-", font=entry_font)
seperator1.place(x=776, y=25)

month_entry = Entry(root, width=3, font=entry_font)
month_entry.place(x=790, y=25)
month_entry.insert(0, month)

seperator1 = Label(root, text="-", font=entry_font)
seperator1.place(x=834, y=25)

day_entry = Entry(root, width=3, font=entry_font)
day_entry.place(x=850, y=25)
day_entry.insert(0, day)


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
    erase_image = Label(root, width=200, height=200)
    erase_image.place(x=1320, y=0)

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
    explanation.place(x=1420, y=150)
    return image_url


def show_image():
    imageUrl = get_image()
    u = urlopen(imageUrl)
    raw_data = u.read()
    u.close()

    # Create image background to erase old image
    erase_image = Label(root, width=200, height=200)
    erase_image.place(x=0, y=65)

    # print photo to window
    image = ImageTk.PhotoImage(data=raw_data)
    label = Label(image=image)
    label.image = image
    label.place(x=15, y=65)


# Print the APOD link
def callback(apod_url):
    webbrowser.open_new_tab(apod_url)


link_font = font.Font(size=14)
link = Label(root, text="APOD link", cursor="hand2", font=link_font)
link.place(x=1080, y=25)
link.bind("<Button-1>", lambda e: callback("https://apod.nasa.gov/apod/astropix.html"))


buttonFont = font.Font(size=16)
imageBtn = Button(
    root, text="Get image", font=buttonFont, command=show_image, cursor="hand2"
)
imageBtn.place(x=920, y=19)

root.mainloop()
