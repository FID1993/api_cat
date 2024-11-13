from tkinter import *
import requests
from PIL import Image, ImageTk
from io import BytesIO


def load_image():
    response = requests.get(url)
    print(response)
    image_data = BytesIO(response.content)
    img = Image.open(image_data)
    img.thumbnail((500, 500))
    img = ImageTk.PhotoImage(img)
    label.config(image=img)
    label.image=img

window = Tk()
window.geometry('500x530')

label = Label()
label.pack()

url = 'https://cataas.com/cat'

mainmenu = Menu(window)
window.config(menu=mainmenu)
file_menu=Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label='Файл', menu=file_menu)
file_menu.add_command(label='Загрузка изображения', command=load_image)
file_menu.add_command(label='Выход', command=window.destroy)


load_image()

window.mainloop()
