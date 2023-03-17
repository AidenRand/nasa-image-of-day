from tkinter import *
from tkinter import font
from PIL import ImageTk
from urllib.request import urlopen
import requests
import json

root = Tk()
root.geometry("800x800")
root.title("Nasa Images")


def get_image():
    url = "https://api.nasa.gov/planetary/apod?api_key=tgdFlsc0ek07wdiX6UI5RDFH0793AzMD5YQi0DWE"

    params = {"hd": "True"}

    # get json data from api
    response = requests.get(url, params=params)
    json_data = json.loads(response.text)
    image_url = json_data["hdurl"]
    return image_url


def show_image():
    imageUrl = get_image()
    u = urlopen(imageUrl)
    raw_data = u.read()
    u.close()

    # print photo to window
    photo = ImageTk.PhotoImage(data=raw_data)
    label = Label(image=photo)
    label.image = photo
    label.place(x=500, y=100)


imageBtn = Button(root, text="Get image", command=show_image)
imageBtn.place(x=300, y=10)

root.mainloop()
