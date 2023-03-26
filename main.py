from tkinter import *
from tkinter import font
from PIL import ImageTk
from urllib.request import urlopen
from datetime import date
import webbrowser
import requests
import json

# Create application window
root = Tk()
root.geometry("1900x1080")
root.title("Nasa Images")
root.config(bg="#d8d8d8")

default_font = font.Font(size=14)
root.option_add("*Font", default_font)

# Get todays date
today = date.today()

year = today.strftime("%Y")
month = today.strftime("%m")
day = today.strftime("%d")


# Create date entries
year_entry = Entry(root, width=6)
year_entry.place(x=700, y=25)
year_entry.insert(0, year)

seperator1 = Label(root, text="-")
seperator1.place(x=776, y=25)

month_entry = Entry(root, width=3)
month_entry.place(x=790, y=25)
month_entry.insert(0, month)

seperator2 = Label(root, text="-")
seperator2.place(x=834, y=25)

day_entry = Entry(root, width=3)
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

    explanation = Text(
        root,
        width=40,
        height=27,
        wrap=WORD,
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


link = Label(root, text="APOD link", cursor="hand2")
link.place(x=1070, y=25)
link.bind("<Button-1>", lambda e: callback("https://apod.nasa.gov/apod/astropix.html"))

imageBtn = Button(root, text="Get image", command=show_image, cursor="hand2")
imageBtn.place(x=920, y=19)

root.mainloop()
