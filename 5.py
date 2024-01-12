from tkinter import *
from tkinter import filedialog
import ImageTk
from PIL import Image, ImageFilter

root = Tk()
root.title("Image to Painting")
root.geometry("700x700")

def open_image():
    global img
    filename = filedialog.askopenfilename(initialdir="/", title="Select Image", filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png"), ("all files", "*.*")))
    img = Image.open(filename)
    newsize = (550, 450)
    img = img.resize(newsize)
    img = img.filter(ImageFilter.CONTOUR)

def save_image():
    filename = filedialog.asksaveasfilename(initialdir="/", title="Save Image", filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png"), ("all files", "*.*")))
    img.save(filename)

def convert_image():
    global img
    img = img.filter(ImageFilter.CONTOUR)
    canvas.delete("all")
    canvas.image = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, anchor=NW, image=canvas.image)

canvas = Canvas(root, width=300, height=300)
canvas.pack()

button_open = Button(root, text="Open Image", command=open_image)
button_open.pack()

button_convert = Button(root, text="Convert to Painting", command=convert_image)
button_convert.pack()

button_save = Button(root, text="Save Image", command=save_image)
button_save.pack()

root.mainloop()