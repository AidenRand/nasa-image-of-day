from tkinter import *
from tkinter import font
from PIL import ImageTk
from urllib.request import urlopen
import requests
import json

root = Tk()
root.geometry("1900x1080")
root.title("Nasa Images")
root.config(bg="#d8d8d8")


def get_image():
    url = "https://api.nasa.gov/planetary/apod?api_key=tgdFlsc0ek07wdiX6UI5RDFH0793AzMD5YQi0DWE"

    params = {"hd": "True"}
    params2 = {"explanation": "True"}

    # get json data from api
    response = requests.get(url, params=params)
    json_data = json.loads(response.text)
    image_url = json_data["url"]

    # Print image explanation
    explanation_font = font.Font(size=14)
    explanation = Text(root, width=130, height=8, wrap=WORD, font=explanation_font)
    explanation.insert(INSERT, json_data["explanation"])
    explanation.place(x=250, y=770)
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
    label.place(x=200, y=80)


buttonFont = font.Font(size=16)
imageBtn = Button(root, text="Get image", font=buttonFont, command=get_image)
imageBtn.place(x=880, y=19)

# Add scrollbar
sb = Scrollbar(root)
sb.pack(side=RIGHT, fill=Y)

root.mainloop()
