from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    global img_path
    img_path = filedialog.askopenfilename(initialdir="/", title="Select an Image", filetypes=(("Image Files", "*.jpg *.jpeg *.png"), ("All Files", "*.*")))
    img = Image.open(img_path)
    img.show()

def save_image():
    global img_path
    img = Image.open(img_path)
    img.save(img_path)

root = Tk()
root.title("Open and Save Image")

btn_open = Button(root, text="Open Image", command=open_image)
btn_open.pack(pady=10)

btn_save = Button(root, text="Save Image", command=save_image)
btn_save.pack(pady=10)

root.mainloop()

