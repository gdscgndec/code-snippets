from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
from pyzbar.pyzbar import decode
import pyqrcode
import os
root = Tk()
root.title("QR code application")
note=ttk.Notebook(root)
note.pack()

frame2=Frame(note, height=400, width=150, bg='white')
frame2.pack(fill="both",expand=True)

canvas2 = Canvas(frame2, width="400", height="400", relief=RIDGE, bd=2)
canvas2.pack(padx=10, pady=10)

def selected():
    img_path = filedialog.askopenfilename(initialdir=os.getcwd(),
                                     title="Select Image", filetype=(
                                         ("PNG file", "*.png"), ("All files", "*.*")))
    img = Image.open(img_path)
    img = ImageTk.PhotoImage(img)
    canvas2.create_image(200, 190, image=img)
    canvas2.image=img                                                                                                                                                                                                                 
    d = decode(Image.open(img_path))
    data = d[0].data.decode()
    qrcode_data = Label(canvas2, text=data, bg='gold', fg='black', font=('ariel 15 bold'), relief=GROOVE)
    qrcode_data.place(x=150, y=380)

btn2 = Button(frame2, text="Select Image", bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE, command=selected)
btn2.pack(side=LEFT, padx=50, pady=5)

root.mainloop()
