from tkinter import *
import requests
from PIL import Image, ImageTk
from io import BytesIO


def load_image(url):
    response = requests.get(url)
    print(response)
    image_data = BytesIO(response.content)
    img = Image.open(image_data)
    win_size = '400x500'
    window.geometry(win_size)
    return ImageTk.PhotoImage(img)

window = Tk()
#window.geometry('500x500')

label = Label()
label.pack()

url = 'https://cataas.com/cat'
img = load_image(url)



if img:
    label.config(image=img)
#    label.image = img

but = Button(text='Загрузка картинки', load_image)
but.pack()

window.mainloop()
